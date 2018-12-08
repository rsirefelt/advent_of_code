(load-file "day1input.el")

(defun first-repeated-frequency (changes)
  (let ((h (make-hash-table :test 'equal)) (f 0))
    (catch 'frequency
      (while t
        (mapc
         (lambda (x)
           (setq f (+ f x))
            (if (gethash f h) (throw 'frequency f) (puthash f f h)))
         changes)))))

(first-repeated-frequency input)
