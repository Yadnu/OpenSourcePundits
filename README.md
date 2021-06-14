# **Technotronics**

---

## Team Members ->

### 1. Jayateerth Shyam Dambal - DKTE

### 2. Tejas Shital Chavan - DKTE

### 3. Shreeraj Yashwantrao Ghorpade - DKTE

### 4. Rupesh Suresh Pawar - DKTE

---

## **This Repo is For Technotronics  Event**

## This project uses Facial Detection and Recognition to record the Attedance of the Clients/Students and Save in a *CSV* File afterwards this File can be Mailed through **SMTP Server** using **yagmail** library of Python

---

## Features of our Project

### We use a CLI Version to commmunicate with our Program. The User can input Choices from 1-5 which Includes these following Features

### 1. Data Generator

#### We use a **dataset** Folder in which 30 Images of Each Client/ Student are stored amd then are used for *Training* our Model

### 2.Face Trainer

#### We use **LBPH** To locate the Binary Histograms of the Face that we detect and then store that elements in a *trainer.yml* File

### 3. Face Recognition

#### In Face Recognition we use the *trainer.yml* File and Predict the Face & and mark the attendance accordingly

### 4. Mailing

### We use **yagmail** library of Python to send mails to a bunch of recepients through SMTP Server

```python

yag.send(
    to=receiver, ## Add the receiver Email To 
    subject=sub, ## Send.
    contents=body,
    attachments=filename
)

 ```

## 5. Mask Detection

### We use Mouth Cascade File to Detect the Mouth of the User and Then we use **Raspberry pi with Servo Motor*** To open the Door For Him

---

## Instructions To Run The Program

### 1. First Clone the Repo by

> git clone https://github.com/JayateerthDambal/Technotronics

### 2. Navigate to the Core folder

`cd Technotronics`

#### **and then install requirements.txt by**

>pip install -r requirements.txt

### 3. Run the **main** File

#### **Windows**

`py main.py`

#### **Linux**

**Python2** --> `python main.py`

**Python3** --> `python3 main.py`

### **4. After recording attendance you can Mail the CSV file of that day to your email Address**

## Made with **❤️** by Students of **DKTE Textile and Engineering Institute, Ichalkaranji**
