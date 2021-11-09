global    start

section   .text
_start:	mov eax, 0x100
	mov ebx, 0x200
	xor ecx, ecx  			; What does this do?
	
	cmp eax, ebx	
	jle label1
	
	cmp eax, 0x100
	je  label2	
	cmp ebx, 0x200
	jne label3  
	mov edx, message1
	jmp print	

label1:
	mov edx, message2
	jmp print	
	
label2:
	mov edx, message3
	jmp print	
label3:
	mov edx, message4
     

print:
        mov       eax, 1                  ; system call for write
        mov       edi, 1                  ; file handle 1 is stdout
        mov       esi, edx                ; address of string to output
        mov       edx, 0x0?               ; number of bytes
        syscall                           ; invoke operating system to do the write

exit:
        mov       rax, 60                 ; system call for exit
        xor       rdi, rdi                ; exit code 0
        syscall                           ; invoke operating system to exit

          section   .data
message1:  db        "fwopCTF{fwee}", 10
message2:  db        "fwopCTF{fwop}", 10
message3:  db        "fwopCTF{flee}", 10
message4:  db        "fwopCTF{foop}", 10


