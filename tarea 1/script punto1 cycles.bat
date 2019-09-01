@ECHO OFF
SET /A start=1
SET fibonnaciNumbers=6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986
::SET /A end=%1
SET /A iterator=1
:while
FOR %%i IN (%fibonnaciNumbers%) DO (
	ECHO Iteracion %%i
	FOR %%j IN (%fibonnaciNumbers%) DO (
		
        IF /I %%j GTR %%i (
		    python "punto1 mcm cycles.py" %%j %%i
	    )
	)
)

::IF /I %iterator% GTR 1 (
::	SET /A iterator=%iterator%*2
::)
::SET /A start=%end%+%iterator%
::SET /A iterator=%iterator%*10
::SET /A end=%iterator%*10-%iterator%
::SET /A iterator=%iterator%/2
::IF /I %start% LEQ %1 (
::	GOTO while
::)
:end
ECHO Terminado