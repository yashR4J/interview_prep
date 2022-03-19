#include <cstdio>
#include <algorithm>
using namespace std

// algorithm, vector, queue, stack, priority

bool is_valid(int day, int month, int year) {
    if (day < 1) return False;
    if (month == 2) {
        if (year % 4 == 0) {
            return day <= 29;
        } else {
            return day <= 28;
        }
    }
    if (month < 1 or month > 12) return False;
}

bool format_valid[6];
int n;
int main() {
    fill(format_valid, format_valid+6, true);
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        int a, b, c;
        scanf("%d/%d/%d", &a, &b, &c);
        if (!is_valid(a, b, c)) format_valid[0] = false;
        if (!is_valid(b, a, c)) format_valid[1] = false;
        if (!is_valid(a, c, b)) format_valid[2] = false;
        if (!is_valid(c, a, b)) format_valid[3] = false;
        if (!is_valid(b, c, a)) format_valid[4] = false;
        if (!is_valid(c, b, a)) format_valid[5] = false;
    }

    int num_valid_formats = 0;
    for (int i = 0; i < 6; i++) {
        num_valid_formats += format_valid[i];
    }
    if (num_valid_formats == 0) {
        printf("Impossible/n");
    } else if (num_valid_formats > 1) {
        printf("Unsure/n");
    } else {
        if (format_valid[0]) printf("DD/MM/YY\n");
        if (format_valid[1]) printf("MM/DD/YY\n");
        if (format_valid[2]) printf("DD/YY/MM\n");
        if (format_valid[3]) printf("YY/DD/MM\n");
        if (format_valid[4]) printf("MM/YY/DD\n");
        if (format_valid[3]) printf("YY/MM/DD\n");
    }
}

