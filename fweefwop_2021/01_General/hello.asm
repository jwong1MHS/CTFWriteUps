          global    _start

          section   .text
_start:   mov       rax, 1                  ; system call for write
          mov       rdi, 1                  ; file handle 1 is stdout 
          mov       rsi, prefix             ; address of string to output
          mov       rdx, 8                  ; number of bytes
          syscall                           ; invoke operating system to do the write

          mov       rax, 1                  ; system call for write
          mov       rdi, 1                  ; file handle 1 is stdout
          mov       rsi, message            ; address of string to output
          mov       rdx, 0x13               ; number of bytes
          syscall                           ; invoke operating system to do the write

          mov       rax, 1                  ; system call for write
          mov       rdi, 1                  ; file handle 1 is stdout
          mov       rsi, postfix            ; address of string to output
          mov       rdx, 0x2                ; number of bytes
          syscall                           ; invoke operating system to do the write

          mov       rax, 60                 ; system call for exit
          xor       rdi, rdi                ; exit code 0
          syscall                           ; invoke operating system to exit

          section   .data
message:  db        "i_have_done_this_exercise_i_swear_but_who_knows" 
prefix:   db        "fwopCTF{"
postfix:  db        "}", 10
