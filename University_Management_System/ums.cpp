#include<iostream>
#include<fstream>
#include<windows.h>
using namespace std;

class University{

    private:
    string RollNo, Name, Subject, Address;

    public:
    University():RollNo(""), Name(""), Subject(""), Address(""){}
    

    void setRollNo(string rollNo){

        RollNo = rollNo;
    }
    void setName(string name){

        Name = name;
    }
    void setSubject(string subject){

        Subject = subject;
    }
    void setAddress(string address){

        Address = address;
    }

    string getRollNo(){

        return RollNo;
    }

    string getName(){

        return Name;
    }

    string getSubject(){

        return Subject;
    }

    string getAddress(){

        return Address;
    }
    
};

void add(University student){
    string rollNo, name, subject, address;

    cout<<"\tEnter RollNo of the Student : ";
    cin >> rollNo;
    student.setRollNo(rollNo);

    cout<<"\tEnter Name of the Student : ";
    cin >> name;
    student.setName(name);

    cout<<"\tEnter Subject of the Student : ";
    cin >> subject;
    student.setSubject(subject);

    cout<<"\tEnter Address of the Student : ";
    cin >> address;
    student.setAddress(address);

    ofstream out("C:/Users/priya/Documents/UMS/university.txt", ios::app);
    if(!out){
        cout<<"\tError : File can't open!"<<endl;
    }
    else{
        out<<"\t"<<student.getRollNo()<<" : "<<student.getName()<<" : "<<student.getSubject()<<" : "<<student.getAddress()<<endl;
    }
    out.close();
    cout<<"\tStudent added successfully!"<<endl;


}

void search(){

    string rollNo;
    cout<<"\tEnter RollNo of the student : ";
    cin >> rollNo;

    ifstream in("C:/Users/priya/Documents/UMS/university.txt");
    if(!in){
        cout<<"\tError : File can't open!"<<endl;
    }
    string line;
    bool found = false;
    while(getline(in, line)){
        int data = line.find(rollNo);

        if(data != string::npos){

            cout<<"\t"<<line<<endl;
            found = true;
        }
        if(!found){
            
            cout<<"\tStudent not found!"<<endl;
        }
    }
    in.close();
}

void update(University student){

    string rollNo;
    cout<<"\tEnter RollNo of the student : ";
    cin >> rollNo;

    ifstream infile("C:/Users/priya/Documents/UMS/university.txt");
    ofstream outfile("C:/Users/priya/Documents/UMS/university temp.txt");
    
    if(!infile || !outfile){
        cout<<"\tError : File can't open!"<<endl;

    }

    string line;
    bool found = false;
    while(getline(infile, line)){

        int pos = line.find(rollNo);
        if(pos != string::npos){
            
            string address;
            cout<<"\tEnter new address : ";
            cin >> address;
            student.setAddress(address);

            int newPos = line.find_last_of(':');
            line.replace(newPos + 2, string::npos, student.getAddress());
        }
        outfile<<line<<endl;
        found = true;
    }
    if(!found){

        cout<<"\tStudent not found!"<<endl;
    }
    outfile.close();
    infile.close();
    remove("C:/Users/priya/Documents/UMS/university.txt");
    rename("C:/Users/priya/Documents/UMS/university temp.txt", "C:/Users/priya/Documents/UMS/university.txt");
    cout<<"\tData updated!"<<endl;
    
}

int main(){

    University Student;

    bool exit = false;

    while(!exit){

        system("cls");

        int val;
        cout<<"\tWelcome to University Management System"<<endl;
        cout<<"\t***************************************"<<endl;
        cout<<"\t1) Add Student"<<endl;
        cout<<"\t2) Search Student"<<endl;
        cout<<"\t3) Update the data of the Student"<<endl;
        cout<<"\t4) Exit."<<endl;
        cout<<"\tEnter Your Choice : ";
        cin >> val;

        if(val == 1){

            system("cls");
            add(Student);
            Sleep(6000);
        }
        else if(val == 2){

            system("cls");
            search();
            Sleep(6000);
        }
        else if(val == 3){

            system("cls");
            update(Student);
            Sleep(6000);
        }
        else if(val == 4){

            system("cls");
            exit = true;
            cout<<"\tHave a good day!"<<endl;
            Sleep(3000);
        }
    }
}