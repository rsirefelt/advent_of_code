(load-file "day3input.el")

(setq tt "#1293 @ 693,199: 25x23")
(setq regexp "^#\\([[:digit:]]+\\) @ \\([[:digit:]]+\\),\\([[:digit:]]+\\): \\([[:digit:]]+\\)x\\([[:digit:]]+\\)$")

(defun get-area (s)
  (let (result x y x0 xs xe ys ye)
    (string-match regexp s)
    (setq xs (string-to-number (match-string 2 s)))
    (setq xe (string-to-number (match-string 4 s)))
    (setq ys (string-to-number (match-string 3 s)))
    (setq ye (string-to-number (match-string 5 s)))
    (setq x (number-sequence xs (+ xs (- xe 1)) 1))
    (setq y (number-sequence ys (+ ys (- ye 1)) 1))
    (mapc
     (lambda (xx)
       (mapc
        (lambda (yy)
          (push (list xx yy) result))
        y))
     x)
    result))

(defun overlapping-hash (prototypes)
  (let ((h (make-hash-table :test 'equal)) (count 0))
    (mapcar
     (lambda (x)
       (mapcar
        (lambda (r)
          (let ((v (gethash r h)))
            (cond ((eq v 1) (puthash r (+ v 1) h))
                  ((eq v nil) (puthash r 1 h))
                  (t nil))))
        (get-area x)))
     prototypes)
    h))

(defun get-number-of-overlaps (prototypes)
  (let ((count 0))
    (maphash
     (lambda (k v)
       (if (> v 1) (setq count (+ count 1)) nil))
     (overlapping-hash prototypes))
    count))
(message "There are %d overlapping square inches" (get-number-of-overlaps input))
