#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc > 0) {
        for (int i = 0; i < argc; i++) {
            printf("%s\n", argv[i]);
        }
    }
    int *ptr = malloc(255);
    printf("%p\n", *ptr);
    if (ptr = NULL) {
        printf("Allocation failed.");
        return 1;
    }
    char mysting[255] = "";
    printf("Enter Text -> ");
    scanf("%s", mysting);
    printf("%s, %i %%", mysting, sizeof(mysting));
    free(ptr);
    ptr = NULL;

}