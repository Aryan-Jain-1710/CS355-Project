# CS355 Project

In this project, we implemented a communication channel and protocol that enables two participants, Alice and Bob, to check if they have any files in common without revealing the contents of the file to one another.


## Protocol Specification
The objective of the protocol is to identify common files between Alice and Bob without revealing the actual file contents of one to the other.
- Alice and Bob are subcontractors (security auditors) of the same company, so they only have access to the code segments they receive from the company.
- Each of them is given ***5*** code-segments in the form of files, each of size ~500MB.
- Both Alice and Bob operate with incredible hostility, so they will exploit any local data they receive through the client-socket channel. They are also unwilling to share the actual contents of their files.
- Adversaries attempting to attack the communication channel are anticipated.



<br/>
<br/>

## Implementation


### Project Structure

- **socket_server.py**: The server side of the application, representing Bob.
- **socket_client.py**: The client side of the application, representing Alice.
- **main.py**: Contains helper functions for hashing contents of input files with SHA-256, and ***sim_check*** for finding overlaps between Alice and Bob's files. 
- **rsa_gen.py**: Contains helper function for RSA key generation

<br/>

### Implementation Details

1. **Key Generation:** Each participant generates their own private and public RSA keys using the `rsa.generate` function from the `PyCryptodome` library.

2. **Key Exchange:** Participants exchange their public RSA keys through the established socket connection.

3. **File Exchange:** For each file, participants send two messages: the hashed value of the file contents using SHA256 and the RSA signature computed for the hashed file using their private RSA key.

4. **Signature Verification:** Upon receiving messages, participants verify the RSA signatures to authenticate the source of each file. If a signature is not verified correctly, all computations are ceased and the connection is closed.

5. **Similarity Check:** After successfully exchanging files, a similarity check is performed using the `sim_check` function, and each participant is shown how many and the contents of which of their files are in common with the other participant.

<br/>

### Dependencies
- **socket**: For client-server communication.
- **PyCryptodome**: For RSA key generation.
- **hashlib**: For SHA-256 hashing.

<br/>

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

<br/>

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




<br/>
<br/>

## Security Analysis

<br/>

### Security Goal


<br/>

### Goal Achieved
