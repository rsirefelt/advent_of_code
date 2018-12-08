(load-file "day2input.el")

(defun get-regexp (c i &optional m)
  (concat "\\(" (char-to-string c) ".*\\)\\{" (number-to-string i) "," (when m (number-to-string m))  "\\}"))

(defun checksum (ids)
  (let ((twos 0) (threes 0))
  (mapc
   (lambda (s)
     (let ((two nil) (three nil))
       (mapc
        (lambda (l)
          (cond ((and (eq two nil) (has-letter-exact-count s l 2) (setq twos (+ twos 1)) (setq two 1)))
                ((and (eq three nil) (has-letter-exact-count s l 3) (setq threes (+ threes 1)) (setq three 1)))
                (t nil)))
       (get-string-with-only-unique-chars s))))
   ids)
  (* twos threes)))

(defun has-letter-appearing (s l min &optional max)
  "s is the string that might contain letter l.
   min is the minimum count of the letter, and max is the maximum count,
   If omitted the maximum bound is infinite"
  (if (string-match (get-regexp l min max) s) 1 nil))

(defun has-letter-exact-count (s l n)
  "s is the string that might contain the character l n times"
  (and (has-letter-appearing s l n n)
       (eq nil (has-letter-appearing s l (+ n 1)))
       1))

(defun get-string-with-only-unique-chars (s)
  (let ((hash (make-hash-table :test 'equal)))
    (mapcar (lambda (x) (puthash x x hash)) s)
    (let ((result ""))
      (maphash
       (lambda (k v) (setq result (concat (char-to-string v) result)))
       hash)
      result)))


(message "Checksum = %d" (checksum input))
