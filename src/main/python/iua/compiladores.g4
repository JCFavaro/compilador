grammar compiladores;

fragment LETRA: [A-Za-z];
fragment DIGITO: [0-9];

PA: '(';
PC: ')';
LLA: '{';
LLC: '}';
PYC: ';';
ASSIG: '=';
COMA: ',';
MULT : '*';
DIV : '/';
SUMA : '+';
RESTA : '-';

INT: 'int';
FLOAT: 'float';
STRING: 'string';

NUMERO: DIGITO+;

ID: (LETRA | '_') (LETRA | DIGITO | '_')*;

WS: [ \t\n\r] -> skip;

OTRO: .;

prog: instrucciones EOF;

instrucciones: instruccion instrucciones |;

instruccion:
	bloque PYC
	| declaracion PYC
	| asignacion PYC
	; // | bloqueif | bloquefor | bloquewhile

bloque: LLA instrucciones LLC;

declaracion:
	tdato ID
	| tdato ID COMA declaracion
	| tdato asignacion
	| ID COMA declaracion // hay que ver esto es el caso int a,b,c,d;  
	| ID
	| asignacion
	| asignacion COMA declaracion;

asignacion: ID ASSIG NUMERO;

tdato: INT | FLOAT | STRING;

// bloquewhile : PA comparacion/opal PC instruccion;

//operacion aritmetica logica opal

itop : oparit itop
	| 
	;

oparit: exp;

exp: term t;

term: factor f;

t:    SUMA term t 
	| RESTA term t 
	|
	;

factor: ID | NUMERO | PA exp PC;

f: MULT factor f 
	| DIV factor f
	|
	;