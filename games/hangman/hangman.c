#include <stdio.h>
#include <stdlib.h>
#include <time.h>

    const char IMG_0[] = 
"   +---+\n"
"   |   |\n"
"       |\n"
"       |\n"
"       |\n"
"       |\n"
"=========\n";
    const char IMG_1[] = 
"   +---+\n"
"   |   |\n"
"   O   |\n"
"       |\n"
"       |\n"
"       |\n"
"=========\n";

    const char IMG_2  [] = 
"   +---+\n"
"   |   |\n"
"   O   |\n"
"  /|   |\n"
"       |\n"
"       |\n"
"=========\n";

    const char IMG_3  [] = 
"   +---+\n"
"   |   |\n"
"   O   |\n"
"  /|\\  |\n"
"       |\n"
"       |\n"
"=========\n";

    const char IMG_4  [] = 
"   +---+\n"
"   |   |\n"
"   O   |\n"
"  /|\\  |\n"
"  /    |\n"
"       |\n"
"=========\n";

    const char IMG_5  [] = 
"   +---+\n"
"   |   |\n"
"   O   |\n"
"  /|\\  |\n"
"  / \\  |\n"
"       |\n"
"=========\n";
    
char *WORDS[6]  = {"limpiar", "cortar", "supercalifrajilistico", "espacios", "lagarto", "spiderman"};
const int MAX_FAIL = 6;


void welcome(){
    printf("###########################################\n");
    printf("##  Bienvenidos al juego del Ahorcado    ##\n");
    printf("###########################################\n");
    printf("\n");
}
 
void good_bye(){
    printf("###########################################\n");
    printf("##      Adios, gracias por participar    ##\n");
    printf("###########################################\n");
    printf("\n");
}     

int rand_number(){
    time_t t;
    int m = 0;
    int n = 7;
    srand((unsigned) time(&t));
    return rand () % (n-m+1) + m;
}
char* get_random_word(){
    int i = rand_number();
    return WORDS[i];
}

int is_letter_in_word(char letter, char *correct_letters, int size){
    for (int i = 0; i < size; i++){
        if (letter == correct_letters[i]){
           return 1;
        }
    }
    return 0;
}

void print_board(int index, char *word, char *correct_letters){

    if (index <= MAX_FAIL && index >= 0 ){
        
        switch (index){
            case 0: printf("%s", IMG_0);
                break;
            case 1: printf("%s", IMG_1);
                break;
            case 2: printf("%s", IMG_2);
                break;
            case 3: printf("%s", IMG_3);
                break;
            case 4: printf("%s", IMG_4);
                break;
            case 5: printf("%s", IMG_5);
                break;
        }
        
        int correct_letters_size = (int) sizeof(correct_letters);

        int word_size = (int) sizeof(word);
        for (int i = 0; i < word_size-1; i++){
            if (is_letter_in_word(word[i], correct_letters, correct_letters_size)){
                printf(" %c ", word[i]);
            }else{
                printf(" _ ");
            }
        }
    }
}


int main()
{
    welcome();
    good_bye();
    char *word;
    char correct_letters[] = {'a'};
    word = get_random_word();
    
    print_board(3, word, correct_letters);
    
    
    return 0;
}
