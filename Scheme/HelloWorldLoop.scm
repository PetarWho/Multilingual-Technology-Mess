(define h "Hello World")
(display h)
(define n (read))
(define printit
   (lambda (x)
      (newline)
      (display h)
      (if (> x 0)
         (printit (- x 1))
      )
   )
)
(printit n)