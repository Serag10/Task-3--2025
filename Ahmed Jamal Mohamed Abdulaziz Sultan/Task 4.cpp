#include <bits/stdc++.h>
using namespace std;

struct Patient {
    string name;
    int bloodSugar;
};

void mergeArrays(vector<Patient>& patients, int left, int mid, int right) {
    int n1 = mid - left + 1,n2 = right - mid;
    vector<Patient> leftArray(n1), rightArray(n2);
    for(int i = 0; i < n1; i++) {
        leftArray[i] = patients[left + i];
    }
    for(int j = 0; j < n2; j++) {
        rightArray[j] = patients[mid + 1 + j];
    }
    int i = 0, j = 0, k = left;
    while(i < n1 && j < n2) {
        if(leftArray[i].bloodSugar >= rightArray[j].bloodSugar) {
            patients[k] = leftArray[i];
            i++;
        } else {
            patients[k] = rightArray[j];
            j++;
        }
        k++;
    }
    while(i < n1) {
        patients[k] = leftArray[i];
        i++;
        k++;
    }
    while(j < n2) {
        patients[k] = rightArray[j];
        j++;
        k++;
    }
}

void mergeSort(vector<Patient>& patients, int left, int right) {
    if(left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(patients, left, mid);
        mergeSort(patients, mid + 1, right);
        mergeArrays(patients, left, mid, right);
    }
}

int main() {
    cout << "Task 4 made by Ahmed Jamal Sultan" << endl;
    vector<Patient> patients = {
        {"Ahmed",   180},
        {"Sara",    90},
        {"Omar",    220},
        {"Layla",   110},
        {"Khaled",  150},
        {"Youssef", 250},
        {"Fatima",  85},
        {"Mahmoud", 195},
        {"Amina",   140},
        {"Hassan",  175}
    };
    mergeSort(patients, 0, patients.size() - 1);
    cout << "Patients sorted by highest blood sugar (descending order) who needs urgent medical help: " << endl;
    for(auto& p : patients) {
        cout << p.name << " - " << p.bloodSugar << " mg/dL\n";
    }
    cout << "\nExplanation:\n";
    cout << "Generally, patients with higher blood sugar levels require more immediate medical attention.\n";
    cout << "In the above data, values above ~126 mg/dL are of greater concern for possible hyperglycemia.\n";
    return 0;
}
