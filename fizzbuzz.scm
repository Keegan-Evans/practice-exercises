;(load "~/repo/simply_scheme/simply.scm")
;(load "~/repo/simply_scheme/functions.scm")
; written for scheme with extensions from simply.scm and functions.scm
; from the simply scheme book. May work on version for generic scheme later.
(define (fizzbuzz)
  (define (divby? divisor outword)
    (lambda (x) (if (= (remainder x divisor) 0)
		    outword
		    '())))
  (define divby3? (divby? 3 'fizz))
  (define divby5? (divby? 5 'buzz))

  (define (each_fizz num)
    (if (> num 100)
	'()
	(se
	  (let ((divs (se (divby3? num)
			  (divby5? num))))
	    (if (empty? divs)
		num
		(accumulate word divs)))
	  (each_fizz (+ num 1)))))

  (each_fizz 1))
