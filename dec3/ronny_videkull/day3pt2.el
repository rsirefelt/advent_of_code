(load-file "day3input.el")
(load-file "day3pt1.el")

(defun get-unique-prototype (prototypes)
  (let ((hash (overlapping-hash prototypes)))
    (catch 'id
      (mapcar
       (lambda (p)
         (if (is-prototype-overlap hash p) nil (throw 'id (match-string 1 p))))
      prototypes))))

(defun is-prototype-overlap (hash p)
  (let ((a nil))
    (catch 'aaa
      (mapcar
       (lambda (x)
         (if (eq (gethash x hash) 1) nil (progn (setq a 1) (throw 'aaa 1))))
       (get-area p))
      a)))

(message "The unique prototype is %s" (get-unique-prototype input))
