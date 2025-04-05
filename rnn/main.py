import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, GRU, Dense
import re
from poems import poems

class PoemPreprocessor:
    def __init__(self, charLevel=True):
        self.charLevel = charLevel
        self.tokenizer = None
        self.maxSequenceLength = None
        self.totalChars = None
        
    def cleanText(self, text):
        """Remove special characters and normalize case"""
        text = text.lower()
        text = re.sub(r'[^a-zA-Z\s\n]', '', text)
        return text
    
    def createSequences(self, cleanedText, sequenceLength=40):
        """Create input-output sequences"""
        sequences = []
        nextChars = []
        
        for i in range(0, len(cleanedText) - sequenceLength):
            sequences.append(cleanedText[i:i + sequenceLength])
            nextChars.append(cleanedText[i + sequenceLength])
            
        return sequences, nextChars
    
    def fitTokenizer(self, texts):
        """Fit tokenizer on texts"""
        if self.charLevel:
            # Character-level tokenization
            allChars = set(''.join(texts))
            self.charToIndex = {char: i for i, char in enumerate(sorted(allChars))}
            self.indexToChar = {i: char for char, i in self.charToIndex.items()}
            self.totalChars = len(allChars)
        else:
            # Word-level tokenization
            self.tokenizer = Tokenizer()
            self.tokenizer.fit_on_texts(texts)
    
    def preprocessData(self, rawTexts, sequenceLength=40):
        """Main preprocessing pipeline"""
        # Clean texts
        cleanedTexts = [self.cleanText(text) for text in rawTexts]
        
        # Fit tokenizer
        self.fitTokenizer(cleanedTexts)
        
        # Create sequences for all texts
        allSequences = []
        allNextChars = []
        
        for text in cleanedTexts:
            sequences, nextChars = self.createSequences(text, sequenceLength)
            allSequences.extend(sequences)
            allNextChars.extend(nextChars)
        
        # Convert to numerical format
        if self.charLevel:
            X = np.zeros((len(allSequences), sequenceLength, self.totalChars), dtype=bool)
            y = np.zeros((len(allSequences), self.totalChars), dtype=bool)
            
            for i, sequence in enumerate(allSequences):
                for t, char in enumerate(sequence):
                    X[i, t, self.charToIndex[char]] = 1
                y[i, self.charToIndex[allNextChars[i]]] = 1
        else:
            X = self.tokenizer.texts_to_sequences(allSequences)
            X = pad_sequences(X, maxlen=sequenceLength)
            y = self.tokenizer.texts_to_sequences(allNextChars)
            y = np.array([item[0] for item in y])
        
        return X, y

def createGruModel(inputShape, outputSize):
    """Create GRU model architecture"""
    model = Sequential([
        GRU(128, input_shape=inputShape, return_sequences=True),
        GRU(128),
        Dense(64, activation='relu'),
        Dense(outputSize, activation='softmax')
    ])
    
    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    
    return model

def main():
    # Initialize preprocessor (character-level)
    preprocessor = PoemPreprocessor(charLevel=True)
    
    # Preprocess all poems
    X, y = preprocessor.preprocessData(poems, sequenceLength=40)
    
    # Create and compile model
    model = createGruModel(
        inputShape=(X.shape[1], X.shape[2]),
        outputSize=y.shape[1]
    )
    
    # Print model summary
    model.summary()
    
    # Train model
    print("\nTraining model...")
    history = model.fit(
        X, y,
        batch_size=128,
        epochs=50,
        validation_split=0.2
    )
    
    def generateText(seedText, numChars=200):
        """Generate new text from trained model"""
        generatedText = seedText
        
        for _ in range(numChars):
            # Prepare the sequence
            sequence = preprocessor.cleanText(generatedText[-40:])
            x = np.zeros((1, 40, preprocessor.totalChars))
            for t, char in enumerate(sequence):
                x[0, t, preprocessor.charToIndex[char]] = 1
            
            # Predict next character
            probs = model.predict(x, verbose=0)[0]
            nextIndex = np.random.choice(len(probs), p=probs)
            nextChar = preprocessor.indexToChar[nextIndex]
            
            generatedText += nextChar
        
        return generatedText
    
    # Generate sample text
    print("\nGenerating sample poem...")
    seedText = "the wind whispers softly"
    generatedPoem = generateText(seedText)
    print(f"\nSeed text: {seedText}")
    print(f"Generated poem:\n{generatedPoem}")

if __name__ == "__main__":
    main()
