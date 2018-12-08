(load-file "day2input.el")

(defun get-regexp (s i)
  (concat (substring s 0 i) "[^" (substring s i (+ i 1)) "]" (substring s (+ i 1) (length s))))

(defun get-regexps (s)
  (let (result)
    (dotimes (number (length s) result) (push (get-regexp s number) result))
    result))

(defun string-match-in-list (list regex)
  (catch 'match
    (mapc
     (lambda (x) (when (string-match regex x) (throw 'match (match-string 0 x))))
     list)
    nil))

(defun common-id (ids)
  (catch 'match
  (mapc
   (lambda (id)
     (mapc
      (lambda (regex)
        (if (string-match-in-list ids regex) (throw 'match (replace-regexp-in-string "\\[^.\\]" "" regex)) nil))
      (get-regexps id)))
   ids)))

(message "The common id is %s" (common-id input))
