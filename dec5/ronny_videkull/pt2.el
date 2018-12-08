(load-file "input.el")
(load-file "pt1.el")
(set (make-local-variable 'case-fold-search) nil) ;; Gaah default value is t...

(defun remove-unit-type (c polymer)
  (replace-regexp-in-string (get-regexp-for-removal-of-char c) "" polymer))

(defun get-regexp-for-removal-of-char (c)
  (concat (char-to-string c) "\\|" (char-to-string (+ c chardiff))))

(defun shortest (polymer)
  (let ((min most-positive-fixnum))
    (mapcar
     (lambda (c)
       (let ((len (length (react (remove-unit-type c polymer)))))
         (if (> min len) (setq min len))))
     (number-sequence 65 90 1))
    min))

(message "The shortest polymer has length: %d" (shortest input))
