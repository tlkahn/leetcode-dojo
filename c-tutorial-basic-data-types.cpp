#include <cmath>
#include <iomanip>
#include <map>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

#include <string.h>
#include <stdio.h>
#include <stdint.h>

#include <bitset>
#include <string>

using namespace std;

long eliminate_unset_bits2(string number)
{
    string res = "";
    for (auto c : number)
    {
        if (c == '1')
        {
            res.push_back(c);
        }
    }
    return std::bitset<64>(res).to_ullong();
}

long eliminate_unset_bits(const char *binary_str)
{
    // TODO: implement this function
    uint64_t number = 0;

    for (int64_t i = strlen(binary_str) - 1; i >= 0; i--)
    {
        if (binary_str[i] == '1')
        {
            number = (number << 1) | 1;
        }
        else if (binary_str[i] != '0')
        {
            // Invalid character found, return -1 as an error
            return -1;
        }
    }
    return number;
}

#define BOOL short
#define YES 1
#define NO 0

char to_uppercase(char c)
{
    if (c >= 'a' && c <= 'z')
    {
        return c - ('a' - 'A');
    }
    return c;
}

#define BOOL short
#define YES 1
#define NO 0
void to_camel_case(const char *text, char *camel)
{
    char *curr = (char *)text;
    BOOL cf = NO;
    while (*curr != '\0')
    {
        if (cf)
        {
            *camel++ = to_uppercase(*curr++);
            cf = NO;
        }
        else if (*curr == '_' || *curr == '|')
        {
            cf = YES;
            curr++;
        }
        else
        {
            *camel++ = *curr++;
        }
    }
    *camel++ = '\0';
}

#include <cctype>

void to_camel_case2(const char *text, char *camel)
{
    bool capitalize = false;
    for (; *text; ++text)
    {
        if (*text == '_' || *text == '|')
        {
            capitalize = true;
        }
        else
        {
            *camel++ = capitalize ? toupper(*text) : *text;
            capitalize = false;
        }
    }
    *camel = '\0';
}

int basicPrint()
{
    int i;
    int64_t l;
    char c;
    float f;
    double d;
    scanf("%d %lld %c %f %lf", &i, &l, &c, &f, &d);
    printf("%d %lld %c %.3f %.9lf", i, l, c, f, d);

    return 0;
}

long eliminate_unset_bits2(string number);

long eliminate_unset_bits(const char *binary_str);

void swapchars(char *p1, char *p2)
{
    char tmp;
    BOOL ef = NO;
    char *oldp2 = p2;
    if (!*p2)
        ef = YES;
    p2--;
    while (p1 < p2)
    {
        tmp = *p1;
        *p1 = *p2;
        *p2 = tmp;
        p1++;
        p2--;
    }
    ef ? *oldp2 = '\0' : *oldp2 = ' ';
}

void spin_words(const char *sentence, char *result)
{
    const char *word_start = sentence;
    while (*sentence)
    {
        if (*sentence == ' ' || *(sentence + 1) == '\0')
        {
            const char *word_end = (*sentence == ' ') ? sentence : sentence + 1;
            if (word_end - word_start >= 5)
            {
                std::reverse_copy(word_start, word_end, result);
            }
            else
            {
                std::copy(word_start, word_end, result);
            }
            result += (word_end - word_start);
            if (*sentence == ' ')
                *result++ = ' ';
            word_start = sentence + 1;
        }
        ++sentence;
    }
    *result = '\0';
}

int get_participants(int handshakes)
{
    int res = handshakes;
    if (!handshakes)
        return 0;
    while (res * (res - 1) / 2 >= handshakes)
        res--;
    return res + 1;
}

class Solution4KeysKeyboard
{
public:
    int maxA(int N)
    {
        if (N <= 5)
        {
            return N;
        }

        std::vector<int> dp(N + 1);
        for (int i = 0; i <= N; ++i)
        {
            dp[i] = i;
        }

        for (int i = 7; i <= N; ++i)
        {
            dp[i] = std::max(dp[i - 4] * 3, dp[i - 5] * 4);
        }

        return dp[N];
    }
};

#include <unordered_set>
#include <stack>

bool valid_braces(std::string braces)
{
    std::unordered_set<char> opens{'(', '[', '{'};
    std::unordered_set<char> closes{')', ']', '}'};
    std::unordered_map<char, char> pairings{{')', '('}, {']', '['}, {'}', '{'}};
    std::stack<char> stack;
    for (auto c : braces)
    {
        if (opens.find(c) != opens.end())
        {
            stack.push(c);
        }
        else if (closes.find(c) != closes.end())
        {
            if (stack.empty() || pairings[c] != stack.top())
            {
                return false;
            }
            stack.pop();
        }
    }
    return true;
}

#include <string>
#include <vector>
#include <sstream>

std::vector<std::string> towerBuilder(int nFloors)
{
    auto res = std::vector<std::string>();
    auto currentline = std::stringstream();
    for (int i = 1; i <= nFloors; i++)
    {
        for (int j = 0; j < nFloors - i; j++)
        {
            currentline << " ";
        }
        for (int j = 0; j < 2 * i - 1; j++)
        {
            currentline << "*";
        }
        for (int j = 0; j < nFloors - i; j++)
        {
            currentline << " ";
        }
        res.push_back(currentline.str());
        currentline.str(std::string());
    }
    return res;
}

string convert_m(char d)
{
    switch (d)
    {
    case 0:
        return "";
    case 1:
        return "M";
    case 2:
        return "MM";
    case 3:
        return "MMM";
    }
    throw "invalid";
}

string convert_c(char d)
{
    switch (d)
    {
    case 0:
        return "";
    case 1:
        return "C";
    case 2:
        return "CC";
    case 3:
        return "CCC";
    case 4:
        return "CD";
    case 5:
        return "D";
    case 6:
        return "DC";
    case 7:
        return "DCC";
    case 8:
        return "DCCC";
    case 9:
        return "CM";
    }
    return "";
}

string convert_x(char d)
{
    switch (d)
    {
    case 0:
        return "";
    case 1:
        return "X";
    case 2:
        return "XX";
    case 3:
        return "XXX";
    case 4:
        return "XL";
    case 5:
        return "L";
    case 6:
        return "LX";
    case 7:
        return "LXX";
    case 8:
        return "LXXX";
    case 9:
        return "XC";
    }
    return "";
}

string convert_i(char d)
{
    switch (d)
    {
    case 0:
        return "";
    case 1:
        return "I";
    case 2:
        return "II";
    case 3:
        return "III";
    case 4:
        return "IV";
    case 5:
        return "V";
    case 6:
        return "VI";
    case 7:
        return "VII";
    case 8:
        return "VIII";
    case 9:
        return "IX";
    }
    return "";
}

std::string solution(int number)
{
    // convert number to string
    short d[4] = {0, 0, 0, 0};
    int i = 0;
    while (number > 0)
    {
        d[i++] = number % 10;
        number = number / 10;
    }
    stringstream ss;
    ss << convert_m(d[3]) << convert_c(d[2]) << convert_x(d[1]) << convert_i(d[0]);
    return ss.str();
}

class DirReduction
{
private:
    enum class dirs : short
    {
        NORTH = 0,
        SOUTH = 1,
        EAST = 2,
        WEST = 3
    };

    static dirs opposite(dirs d)
    {
        switch (d)
        {
        case dirs::NORTH:
            return dirs::SOUTH;
        case dirs::SOUTH:
            return dirs::NORTH;
        case dirs::EAST:
            return dirs::WEST;
        case dirs::WEST:
            return dirs::EAST;
        }
        throw "invalid";
    }

public:
    static std::vector<std::string> dirReduc(std::vector<std::string> &arr)
    {
        std::unordered_set<dirs> res;
        for (auto d : arr)
        {
            // convert string d to dirs
            dirs dir;
            if (d == "NORTH")
            {
                dir = dirs::NORTH;
            }
            else if (d == "SOUTH")
            {
                dir = dirs::SOUTH;
            }
            else if (d == "EAST")
            {
                dir = dirs::EAST;
            }
            else if (d == "WEST")
            {
                dir = dirs::WEST;
            }
            else
            {
                throw "invalid";
            }

            if (res.empty())
            {
                res.insert(dir);
            }
            else
            {
                auto opposite_index = res.find(opposite(dir));
                if (opposite_index != res.end())
                {
                    res.erase(opposite_index);
                }
                else
                {
                    res.insert(dir);
                }
            }
        }
        vector<string> res_vec;
        for (auto d : res)
        {
            switch (d)
            {
            case dirs::NORTH:
                res_vec.push_back("NORTH");
                break;
            case dirs::SOUTH:
                res_vec.push_back("SOUTH");
                break;
            case dirs::EAST:
                res_vec.push_back("EAST");
                break;
            case dirs::WEST:
                res_vec.push_back("WEST");
                break;
            }
        }
        return res_vec;
    }
};

long queueTime(std::vector<int> customers, int n)
{
    std::vector<int> tills(n, 0);
    for (auto c : customers)
    {
        auto min_index = std::min_element(tills.begin(), tills.end());
        *min_index += c;
    }
    return *std::max_element(tills.begin(), tills.end());
}

bool narcissistic(int value)
{
    // get all digits from int value
    std::vector<int> digits;
    int tmp = value;
    while (tmp > 0)
    {
        digits.push_back(tmp % 10);
        tmp /= 10;
    }
    // calculate sum of each digit to the power of number of digits
    int sum = 0;
    for (auto d : digits)
    {
        int tmp = 1;
        for (uint64_t i = 0; i < digits.size(); i++)
        {
            tmp *= d;
        }
        sum += tmp;
    }
    return sum == value;
}

#include <cmath>

bool narcissistic2(int value)
{
    int tmp = value;
    int sum = 0;
    int numDigits = static_cast<int>(std::log10(value)) + 1;

    while (tmp > 0)
    {
        int digit = tmp % 10;
        sum += std::pow(digit, numDigits);
        tmp /= 10;
    }

    return sum == value;
}

void splitString(const std::string &input, std::string &prefix, std::string &suffix)
{
    size_t pos = input.find_last_not_of("0123456789");
    prefix = input.substr(0, pos + 1);
    suffix = input.substr(pos + 1);
}

std::string stringToInt(const std::string &digits)
{
    if (digits.empty())
        return "1";
    // return a string represents digits plus one while keeping the leading zeros
    std::string res;
    int cf = 1;
    for (int i = digits.size() - 1; i >= 0; i--)
    {
        int tmp = digits[i] - '0' + cf;
        cf = tmp / 10;
        res.insert(res.begin(), tmp % 10 + '0');
    }
    if (cf)
        res.insert(res.begin(), '1');
    return res;
}

std::string incrementString(const std::string &str)
{
    std::string prefix, suffix;
    splitString(str, prefix, suffix);
    auto res = stringToInt(suffix);
    return prefix + res;
}

class Same
{
private:
    static bool isAlmostEqualToInt(double num, double tolerance = 1e-6)
    {
        int nearestInt = static_cast<int>(std::round(num));
        return std::abs(num - nearestInt) <= tolerance;
    }
    static int basicroot(int a)
    {
        double sqrta = std::sqrt(a);
        if (Same::isAlmostEqualToInt(sqrta))
            return Same::basicroot(std::round(sqrta));
        else
            return a;
    }

public:
    static bool comp(std::vector<int> &a, std::vector<int> &b)
    {
        std::unordered_map<int, int> counter_a;
        std::unordered_map<int, int> counter_b;

        for (int k : a)
        {
            counter_a[Same::basicroot(k)]++;
        }
        for (int k : b)
        {
            counter_b[Same::basicroot(k)]++;
        }
        // check if counter_a and counter_b have the same keys and same values for a given key
        for (auto &p : counter_a)
        {
            if (counter_b.find(p.first) == counter_b.end() || counter_b[p.first] != p.second)
            {
                return false;
            }
        }
        return true;
    }
};

class Solution
{
private:
    int getAnagramSig(const std::string &a)
    {
        short char_count[26] = {0};
        for (char c : a)
        {
            char_count[c - 'a']++;
        }
        int sig = 0;
        for (int i = 0; i < 26; i++)
        {
            sig += (char_count[i] >> i);
        }
        return sig;
    }
    bool areAnagrams(const std::string &str1, const std::string &str2)
    {
        if (str1.length() != str2.length())
        {
            return false;
        }

        int char_count[26] = {0};

        for (char c : str1)
        {
            char_count[c - 'a']++;
        }

        for (char c : str2)
        {
            char_count[c - 'a']--;
        }

        for (int count : char_count)
        {
            if (count != 0)
            {
                return false;
            }
        }
        return true;
    }

    unordered_map<int, vector<string>> groupBy(vector<string> &strs, function<int(const string &)> func)
    {
        std::unordered_map<int, std::vector<string>> groups;

        for (string s : strs)
        {
            int key = func(s);
            groups[key].push_back(s);
        }

        return groups;
    }

public:
    vector<vector<string>> groupAnagrams(vector<string> &strs)
    {
        vector<vector<string>> res;
        for (auto s : strs)
        {
            bool found = false;
            for (auto &v : res)
            {
                if (areAnagrams(s, v[0]))
                {
                    v.push_back(s);
                    found = true;
                    break;
                }
            }
            if (!found)
            {
                res.push_back({s});
            }
        }
        return res;
    }
};

bool isPrime(int n)
{
    if (n < 2)
        return false;
    for (int i = 2; i < sqrt(n) + 1; i++)
    {
        if ((double)n / i - n / i < 0.001)
            return false;
    }
    return true;
}

std::map<char, unsigned> count(const std::string &string)
{
    std::map<char, unsigned> res;
    for (char c : string)
    {
        if (res.find(c) == res.end())
        {
            res[c] = 1;
        }
        else
        {
            res[c]++;
        }
    }
    return res;
}

std::vector<int> deleteNth(std::vector<int> arr, int n)
{
    std::unordered_map<int, int> counter;
    std::vector<int> res;
    for (auto i : arr)
    {
        if (counter.find(i) == counter.end())
        {
            counter[i] = 1;
            res.push_back(i);
        }
        else if (counter[i] < n)
        {
            counter[i]++;
            res.push_back(i);
        }
    }
    return res;
}

#define TRUNC_RGB(x) (x < 0 ? 0 : (x > 255 ? 255 : x)

class RGBToHex
{
public:
    static std::string rgb(int r, int g, int b)
    {
        std::stringstream ss;
        ss << std::hex << std::uppercase << std::setfill('0') << std::setw(2) << std::clamp(r, 0, 255) << std::setw(2) << std::clamp(g, 0, 255) << std::setw(2) << std::clamp(b, 0, 255);
        return ss.str();
    }
};

std::vector<int> snail(const std::vector<std::vector<int>> &snail_map)
{
    std::vector<int> res;
    if (snail_map.empty() || snail_map[0].empty())
        return res;
    int n = snail_map.size();
    int i = 0, j = 0;
    int direction = 0;
    int left = 0, right = n - 1, top = 0, bottom = n - 1;
    while (left <= right && top <= bottom)
    {
        res.push_back(snail_map[i][j]);
        switch (direction)
        {
        case 0:
            if (j == right)
            {
                direction = 1;
                top++;
                i++;
            }
            else
            {
                j++;
            }
            break;
        case 1:
            if (i == bottom)
            {
                direction = 2;
                right--;
                j--;
            }
            else
            {
                i++;
            }
            break;
        case 2:
            if (j == left)
            {
                direction = 3;
                bottom--;
                i--;
            }
            else
            {
                j--;
            }
            break;
        case 3:
            if (i == top)
            {
                direction = 0;
                left++;
                j++;
            }
            else
            {
                i--;
            }
            break;
        }
    }
    return res;
}

std::vector<int> snail2(const std::vector<std::vector<int>> &snail_map)
{
    std::vector<int> res;
    if (snail_map.empty() || snail_map[0].empty())
        return res;

    int n = snail_map.size();
    int i = 0, j = 0, direction = 0, left = 0, right = n - 1, top = 0, bottom = n - 1;

    while (left <= right && top <= bottom)
    {
        res.push_back(snail_map[i][j]);

        switch (direction)
        {
        case 0:
            j == right ? (++direction, ++top, ++i) : ++j;
            break;
        case 1:
            i == bottom ? (++direction, --right, --j) : ++i;
            break;
        case 2:
            j == left ? (++direction, --bottom, --i) : --j;
            break;
        case 3:
            i == top ? (direction = 0, ++left, ++j) : --i;
            break;
        }
    }

    return res;
}

std::string sum_strings(const std::string &a, const std::string &b)
{
    std::string res;
    int cf = 0;
    int i = a.size() - 1, j = b.size() - 1;
    while (i >= 0 || j >= 0)
    {
        int tmp = cf;
        if (i >= 0)
        {
            tmp += a[i] - '0';
            i--;
        }
        if (j >= 0)
        {
            tmp += b[j] - '0';
            j--;
        }
        cf = tmp / 10;
        res.insert(res.begin(), tmp % 10 + '0');
    }
    if (cf)
        res.insert(res.begin(), '1');
    return res;
}

std::vector<std::vector<int>> matrix_multiplication(std::vector<std::vector<int>> &a, std::vector<std::vector<int>> &b, size_t n)
{
    // Return the result of A × B in the form of an n × n matrix C
    // Please allocate and return matrix C
    std::vector<std::vector<int>> res(n, std::vector<int>(n, 0));
    for (size_t i = 0; i < n; i++)
    {
        for (size_t j = 0; j < n; j++)
        {
            for (size_t k = 0; k < n; k++)
            {
                res[i][j] += a[i][k] * b[k][j];
            }
        }
    }
    return res;
}

int main()
{
}
