grammar compiladores;

fragment LETRA: [A-Za-z];
fragment DIGITO: [0-9];

//Operadores
PA: '(';
PC: ')';
LLA: '{';
LLC: '}';
PYC: ';';
COMA: ',';

//Operaciones aritmeticas
MULT: '*';
DIV: '/';
SUMA: '+';
RESTA: '-';
MOD: '%';

//Operaciones logicas
AND: '&&';
OR: '||';
NOT: '!';
ASSIG: '=';

//Comparadores
IGUAL: '==';
DISTINTO: '!=';
MENOR: '<';
MENORIGUAL: '<=';
MAYOR: '>';
MAYORIGUAL: '>=';


//Tipo de datos
INT: 'int';
FLOAT: 'float';
STRING: 'string';
DOUBLE: 'double';

//Estructuras de control
IF: 'if';
FOR: 'for';
WHILE: 'while';

//Funciones
RETURN: 'return';

NUMERO: DIGITO+;

ID: (LETRA | '_') (LETRA | DIGITO | '_')*;

WS: [ \t\n\r] -> skip;

OTRO: .;

prog: instrucciones EOF;

instrucciones: 	instruccion instrucciones 
				|
				;

instruccion:
	bloque PYC
	| declaracion COMA
	| declaracion PYC
	| asignacion PYC
	| bloqueif; // | bloquefor | bloquewhile

bloque: LLA instrucciones LLC;

declaracion:
	tdato ID 
	| tdato ID asignacion
	| tdato ID 
	| tdato asignacion 
	| ID  // hay que ver esto es el caso int a,b,c,d;  
	| ID
	| asignacion
	| asignacion COMA;

asignacion: ID ASSIG NUMERO | ID ASSIG ID;

tdato: INT | FLOAT | STRING | DOUBLE;

oprelacionales: IGUAL 
				| DISTINTO
				| MENOR
				| MAYOR
				| AND
				| OR
				;

comparacion: ID oprelacionales NUMERO
			| NUMERO oprelacionales ID
			| ID oprelacionales ID
			;

condicion: PA comparacion PC;

bloqueif : IF condicion			
			;

// bloquewhile : PA comparacion/opal PC instruccion;

//operacion aritmetica logica opal

itop: 	oparit itop 
		| EOF
		;

oparitlog: predicado;

predicado: |;

oparit: exp;

exp: term t;

term: factor f;

t: 	SUMA term t 
	| RESTA term t 
	| OR term t 
	| factor
	|
	;

factor: ID 
		| NUMERO 
		| PA exp PC
		;

f: 	MULT factor f 
	| DIV factor f 
	| AND factor f 
	| MOD factor f 
	|
	;

//Funciones
