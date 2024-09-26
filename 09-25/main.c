#include <windows.h>
#include <stdlib.h>

HANDLE ScreenBuffH = NULL;


void exit1(void) {
    //CloseHandle(ScreenBuffH);
}

void clearScreen() {
    WriteConsole(ScreenBuffH, "\033[2J", sizeof("\033[2J"), NULL, NULL);
}

int main(int argc, char* argv) {
    ScreenBuffH = GetStdHandle(STD_OUTPUT_HANDLE);
    char mestr[] = "Hello there!";
    atexit(exit1);
    WriteConsole(ScreenBuffH, mestr, sizeof(mestr), NULL, NULL);
    return 0;
}

