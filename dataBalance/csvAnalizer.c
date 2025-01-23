#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_LINE 1024
#define MAX_ASSOCIATIONS 50
#define MAX_NAME_LENGTH 50

typedef struct {
    char name[MAX_NAME_LENGTH];
    int count;
} Association;

// Function to trim whitespace and convert to lowercase
void cleanString(char *str) {
    // Remove leading whitespace
    char *start = str;
    while(isspace((unsigned char)*start)) start++;
    
    if(start != str) {
        memmove(str, start, strlen(start) + 1);
    }
    
    // Remove trailing whitespace
    char *end = str + strlen(str) - 1;
    while(end > str && isspace((unsigned char)*end)) end--;
    *(end + 1) = '\0';
    
    // Convert to lowercase
    for(int i = 0; str[i]; i++) {
        str[i] = tolower((unsigned char)str[i]);
    }
}

// Function to find association in array
int findAssociation(Association *assocs, int count, const char *name) {
    for(int i = 0; i < count; i++) {
        if(strcmp(assocs[i].name, name) == 0) {
            return i;
        }
    }
    return -1;
}

int main() {
    char filename[256];
    char column_name[MAX_NAME_LENGTH];
    char line[MAX_LINE];
    char *token;
    Association associations[MAX_ASSOCIATIONS] = {0};
    int assoc_count = 0;
    
    // Get input from user
    printf("Enter CSV filename: ");
    scanf("%255s", filename);
    
    printf("Enter column name to analyze (e.g., association): ");
    scanf("%49s", column_name);
    
    // Convert column name to lowercase immediately
    char lowercase_column_name[MAX_NAME_LENGTH];
    strncpy(lowercase_column_name, column_name, MAX_NAME_LENGTH - 1);
    lowercase_column_name[MAX_NAME_LENGTH - 1] = '\0';
    cleanString(lowercase_column_name);
    
    // Open file
    FILE *file = fopen(filename, "r");
    if (!file) {
        printf("Error opening file!\n");
        return 1;
    }
    
    // Read header line to find column index
    if (!fgets(line, MAX_LINE, file)) {
        printf("Error reading header!\n");
        fclose(file);
        return 1;
    }
    
    // Find column index
    int target_col = -1;
    int current_col = 0;
    char *header_copy = strdup(line);
    token = strtok(header_copy, ",");
    
    while(token) {
        char clean_token[MAX_NAME_LENGTH];
        strncpy(clean_token, token, MAX_NAME_LENGTH - 1);
        clean_token[MAX_NAME_LENGTH - 1] = '\0';
        cleanString(clean_token);
        
        if(strcmp(clean_token, lowercase_column_name) == 0) {
            target_col = current_col;
            break;
        }
        current_col++;
        token = strtok(NULL, ",");
    }
    free(header_copy);
    
    if(target_col == -1) {
        printf("Column '%s' not found in CSV!\n", column_name);
        fclose(file);
        return 1;
    }
    
    // Process data lines
    while(fgets(line, MAX_LINE, file)) {
        current_col = 0;
        token = strtok(line, ",");
        
        while(token && current_col <= target_col) {
            if(current_col == target_col) {
                char clean_value[MAX_NAME_LENGTH];
                strncpy(clean_value, token, MAX_NAME_LENGTH - 1);
                clean_value[MAX_NAME_LENGTH - 1] = '\0';
                cleanString(clean_value);
                
                int index = findAssociation(associations, assoc_count, clean_value);
                if(index >= 0) {
                    associations[index].count++;
                } else if(assoc_count < MAX_ASSOCIATIONS) {
                    strncpy(associations[assoc_count].name, clean_value, MAX_NAME_LENGTH - 1);
                    associations[assoc_count].name[MAX_NAME_LENGTH - 1] = '\0';
                    associations[assoc_count].count = 1;
                    assoc_count++;
                }
                break;
            }
            current_col++;
            token = strtok(NULL, ",");
        }
    }
    
    fclose(file);
    
    // Find most and least frequent
    if(assoc_count == 0) {
        printf("No associations found!\n");
        return 1;
    }
    
    int max_index = 0;
    int min_index = 0;
    
    for(int i = 1; i < assoc_count; i++) {
        if(associations[i].count > associations[max_index].count) {
            max_index = i;
        }
        if(associations[i].count < associations[min_index].count) {
            min_index = i;
        }
    }
    
    // Print results
    printf("\nResults:\n");
    printf("Most frequent: %s (%d occurrences)\n", 
           associations[max_index].name, associations[max_index].count);
    printf("Least frequent: %s (%d occurrences)\n", 
           associations[min_index].name, associations[min_index].count);
    
    return 0;
}
