;(load "~/repo/simply_scheme/simply.scm")
;(load "~/repo/simply_scheme/functions.scm")
; written for scheme with extensions from simply.scm and functions.scm
; from the simply scheme book. May work on version for generic scheme later.
(define (fizzbuzz)
  (define (divby? divisor outword)
    (lambda (x) (if (= (remainder num divisor) 0)
		    outword
		    '())))
  (define divby3? (divby? 3 'fizz))
  (define divby5? (divby? 5 'buzz))

  (define (each_fizz num)
    (if (> num 100)
	""
	(se 
	  ((lambda (each) ()))))))
