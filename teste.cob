IDENTIFICATION DIVISION.
PROGRAM-ID. SomaNumeros.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 Numero1 PIC 9(5).
01 Numero2 PIC 9(5).
01 Soma PIC 9(6).

PROCEDURE DIVISION.
    DISPLAY "Digite o primeiro número: " WITH NO ADVANCING.
    ACCEPT Numero1.
    DISPLAY "Digite o segundo número: " WITH NO ADVANCING.
    ACCEPT Numero2.

    COMPUTE Soma = Numero1 + Numero2.

    DISPLAY "A soma de " Numero1 " e " Numero2 " é: " Soma.
    STOP RUN.
