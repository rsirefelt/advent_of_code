(load-file "input.el")
(setq chardiff 32)

(defun react (s)
  (let (ss)
    (catch 'aaa
      (let ((i 0))
        (while t
          (cond ((eq (length s) i) (throw 'aaa nil))
                ((eq (abs (- (elt s i) (if ss (nth 0 ss) 0))) chardiff) (pop ss))
                (t (push (elt s i) ss)))
          (setq i (+ 1 i)))))
    ss))
(message "Length is %d" (length (react input))
