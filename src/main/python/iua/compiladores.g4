grammar compiladores;

fragment LETRA : [A-Za-z] ;
fragment DIGITO : [0-9] ;

PA : '(' ;
PC : ')' ;
LLA : '{';
LLC : '}';
PYC : ';';
ASSIG : '=';
COMA : ',';

INT : 'int';

NUMERO : DIGITO+ ;

ID : (LETRA | '_')(LETRA | DIGITO | '_')* ;

WS : [ \t\n\r] -> skip ; 

OTRO : . ;

prog : instrucciones EOF;

instrucciones : instruccion instrucciones
              |
              ;

instruccion : bloque PYC
            | declaracion PYC
            | asignacion PYC
            // | bloqueif
            // | bloquefor
            // | bloquewhile
            ;

bloque : LLA instrucciones LLC;

declaracion : tdato ID 
            | tdato asignacion
            | ID COMA declaracion // hay que ver esto es el caso int a,b,c,d;  
            | ID declaracion             
            | asignacion
            ;

asignacion : ID ASSIG NUMERO;

tdato : INT;

// bloquewhile : PA comparacion/opal PC instruccion;

//operacion aritmetica logica opal