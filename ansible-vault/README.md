# Introduction to Ansible Vault #

An Introductory tutorial to Ansible Vault. You can try running the encrypted file uploaded in the repository. The password for thr file is `fedora`

## Introduction ##

Ansible Vault is a feature of ansible that allows you to keep sensitive data such as passwords or keys in encrypted files, rather than as plaintext in playbooks or roles. These vault files can then be distributed or placed in source control.

## Using Ansible Vault ##

### NOTE: For this tutorial, I'll be using a simple playbook that will add two new users to the system. ###

### Encrypting a Playbook ###

To encrypt an existing ansible playbook, run the following command:

```
$ ansible-vault encrypt users.yml
```

### Viewing an Encrypted Playbook ###
If you want to view the contents of an encrypted file without editing it, you can use the ansible-vault view command:

```
$ ansible-vault view users.yml
```

### Editing an Encrypted Playbook ###

To edit an encrypted file in place, use the ansible-vault edit command. This command will decrypt the file to a temporary file and allow you to edit the file, saving it back when done and removing the temporary file:

```
$ ansible-vault edit users.yml 
```

### Running a Playbook with Vault ###

To run a playbook that contains vault-encrypted data files, you must provide the vault password.

- To specify the vault-password interactively:

```
$ ansible-playbook -K users.yml --ask-vault-pass
```

- Alternatively, passwords can be specified with a file or a script (the script version will require Ansible 1.7 or later). When using this flag, ensure permissions on the file are such that no one else can access your key and do not add your key to source control:

```
$ ansible-playbook -K users.yml --vault-password-file vault-passwd
```

### Changing Vault Password ###

If you wish to change your password on a vault-encrypted file or files, you can do so with the rekey command:

```
$ ansible-vault rekey users.yml
```

### Decrypting the Playbook ###

If you have existing files that you no longer want to keep encrypted, you can permanently decrypt them by running the ansible-vault decrypt command. This command will save them unencrypted to the disk, so be sure you do not want ansible-vault edit instead:

```
$ ansible-vault decrypt users.yml 
```

## Video Tutorial ##

[![asciicast](https://asciinema.org/a/hry7UI8VL2duuLji0ncAtPlnp.png)](https://asciinema.org/a/hry7UI8VL2duuLji0ncAtPlnp)
