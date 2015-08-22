/* Code Eval - Even Numbers
 * https://www.codeeval.com/open_challenges/100/
 */

#include <stdio.h>

int main(int argc, const char * argv[]) {
    FILE *file = fopen(argv[1], "r");
    char line[1024];
    while (fgets(line, 1024, file)) {
        int number = atoi(line);
        printf("%d\n", !(number%2));
    }
    return 0;
}
