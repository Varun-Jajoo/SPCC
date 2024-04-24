%{
int c = 0;
int l = 0;
int s = 0;
int w = 0;
%}

%%
[\n] { l++; }
[\t] { s++; }
[a-zA-Z]+ { w++; c += strlen(yytext); }
. { c++; }
%%

int yywrap() { return 1; }

void main() {
    printf("Enter a sentence: ");
    yylex();
    printf("\nCharacters: %d\n", c);
    printf("Lines: %d\n", l);
    printf("Tabs: %d\n", s);
    printf("Words: %d\n", w);
}

