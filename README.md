# CS355 Project

In this project, we implemented a communication channel and protocol that enables two participants, Alice and Bob, to check if they have any files in common without revealing the contents of the files to one another.

<br/>

# Protocol Specification
The protocol's objective is to identify common files between Alice and Bob without revealing the actual file contents of one to the other.
- Alice and Bob are subcontractors (security auditors) of the same company, so they only have access to the code segments they receive from the company.
- Each of them is given ***5*** code-segments in the form of files, each of size ~500MB.
- Both Alice and Bob operate with incredible hostility, so they will exploit any local data they receive through the client-socket channel. They are also unwilling to share the actual contents of their files.
- Adversaries attempting to attack the communication channel are anticipated.

---

<br/>

# Implementation


### Project Structure:

- **socket_server.py**: The server side of the application, representing Bob.
- **socket_client.py**: The client side of the application, representing Alice.
- **main.py**: Contains helper functions for hashing contents of input files with SHA-256, and `sim_check2()` for finding overlaps between Alice and Bob's files. 
- **rsa_gen.py**: Contains helper function for RSA key generation
---

### Procedure:

1. **Key Generation:** Each participant generates their own private and public RSA keys using the `rsa.generate()` function from the `PyCryptodome` library.

2. **Key Exchange and Verification:** Participants exchange their public RSA keys through the established socket connection. They also send the received public keys back to each other for verification. The connection is terminated if public key verification fails, i.e. if the public key sent back doesn't match the public key in their possession that they sent out.

3. **File Exchange:** For each file, participants send two messages: the hashed value of the file contents using SHA256 and the RSA signature computed for the hashed file using their private RSA key.

4. **Signature Verification:** Upon receiving messages, participants verify the RSA signatures to authenticate the source of each file. If a signature is not verified correctly, all computations are ceased and the connection is closed.

5. **Similarity Check:** After successfully exchanging files, a similarity check is performed using the `sim_check2()` function, and each participant is shown how many and the contents of which of their files are in common with the other participant.

---
### Dependencies
- **socket**: For client-server communication.
- **PyCryptodome**: For RSA key generation.
- **hashlib**: For SHA-256 hashing.

---
### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/Aryan-Jain-1710/CS355-Project.git
    cd CS355-Project
    ```

2. Install the required dependencies:

    ```bash
    pip install pycryptodome
    ```

---
### How to Run

1. Run the server:

    ```bash
    python socket_server.py
    ```

2. Run the client:

    ```bash
    python socket_client.py
    ```

3. Follow the prompts to enter the names of 5 files.

4. The files will be securely exchanged between the participants, and the results of the file similarity check will be displayed for each participant.

---
### References

-  https://cryptobook.nakov.com/digital-signatures/rsa-sign-verify-examples
   - for RSA Digital Signature Implementation  
-  https://realpython.com/python-sockets/
   -  for socket programming in python

---

<br/>

# Security Analysis (Security Goals and How They Are Achieved)

### 1. Confidentiality: Compare files without revealing file contents 
- **Objective:** Enable Alice and Bob to identify common files without disclosing the actual contents of their files to one another.
- **Achieved By:** The contents of files are hashed using SHA256, an irreversible, one-way hashing algorithm, before being sent through the client-server channel. Moreover, Alice and Bob only have access to the files they are given as subcontractors of the company, so they don't have access to any other files, which prevents them from brute-forcing the hashing algorithm on the company's codebase.

---
### 2. Secure Public Key Exchange
- **Objective:** Ensure the secure exchange of public keys, preventing man-in-the-middle attacks.
- **Achieved By:** Alice and Bob exchange public keys securely through the client-server socket connection. They also send the public keys they receive back for verification from the sender. The connection is terminated if the public key received back doesn't match the public key in their possession that they sent.

---
### 3. Authentication: Ensure hashed file content is exchanged between Alice and Bob only
- **Objective:** Authenticate files to prevent unauthorized access and ensure data integrity.
- **Achieved By:** Files are authenticated using RSA signatures. Any anomaly in communication or failure in signature verification results in the termination of the connection.

---
### 4. Limited Knowledge: Learn only about similarity results in the context of files Alice/Bob themselves possess
- **Objective:** Restrict the information revealed through similarity results specific to the files possessed by Alice and Bob.
- **Achieved By:** The `sim_check2()` function is used to display results tailored to the names of files owned by each participant that they have in common with the other, preventing the disclosure of any information about the other participant's files (including not even revealing the other party's file name).

---
### `Note:` These security measures collectively provide a robust framework for secure file exchange and communication between Alice and Bob.

<br/>
