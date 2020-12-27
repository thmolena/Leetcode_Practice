string
addStrings(string
num1, string
num2) {
    int
num1_len = num1.length() - 1;
int
num2_len = num2.length() - 1;
int
carry = 0;
int
needed = '0';
string
req_sol = "";
while (num1_len >= 0 | | num2_len >= 0){
int current_num1 = (num1_len >= 0) ? num1.at(num1_len)-'0':0;
int
current_num2 = (num2_len >= 0)? num2.at(num2_len) - '0': 0;

int
current_val = current_num1 + current_num2 + carry;
cout << "curentval" << current_val << endl;

if (current_val >= 9)
{
    needed = current_val % 10;
}
else {
    needed = current_val;
}


req_sol = to_string(needed) + req_sol;
if (current_val > 9)
{
    carry = 1;
}
else {
    carry = 0;
}
num1_len - -;
num2_len - -;
needed = '0';

}

if (carry == 1){
req_sol = to_string(carry) + req_sol;
}
return req_sol;
}