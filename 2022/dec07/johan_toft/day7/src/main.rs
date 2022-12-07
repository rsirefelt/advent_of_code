use std::collections::HashMap;

struct File {
    name: String,
    size: u64,
}

impl Clone for File {
    fn clone(&self) -> Self {
        File {
            name: self.name.clone(),
            size: self.size,
        }
    }
}

use std::cell::RefCell;
use std::clone;
use std::rc::Rc;

struct Directory {
    name: String,
    files: Vec<File>,
    directories: HashMap<String, Rc<RefCell<Directory>>>,
    parent: Option<Rc<RefCell<Directory>>>,
}

impl Clone for Directory {
    fn clone(&self) -> Self {
        Directory {
            name: self.name.clone(),
            files: self.files.clone(),
            directories: self.directories.clone(),
            parent: self.parent.clone(),
        }
    }
}

struct FileSystem {
    root: Rc<RefCell<Directory>>,
}

impl Directory {
    fn new(name: &str, parent: Option<Rc<RefCell<Directory>>>) -> Directory {
        Directory {
            name: name.to_string(),
            files: Vec::new(),
            directories: HashMap::new(),
            parent: parent,
        }
    }

    fn add_file(&mut self, file: File) {
        self.files.push(file);
    }

    fn add_directory(&mut self, directory: Rc<RefCell<Directory>>) {
        let name : String = directory.borrow().name.clone();
        if self.directories.contains_key(&name) {
        } else {
            self.directories.insert(name, directory);
        }
    }

    fn size(&self) -> u64 {
        self.files.iter().map(|f| f.size).sum::<u64>() +
            self.directories.values().map(|d| d.borrow().size()).sum::<u64>()
    }

    fn get_all_directories(&self) -> Vec<Rc<RefCell<Directory>>> {
        let mut directories : Vec<Rc<RefCell<Directory>>> = Vec::new();
        for (_, directory) in self.directories.iter() {
            directories.push(directory.clone());
            directories.append(&mut directory.borrow().get_all_directories());
        }
        directories
    }
}


impl FileSystem {
    fn new() -> FileSystem {
        FileSystem {
            root: Rc::new(RefCell::new(Directory::new("root", None))),
        }
    }

    fn parse_cmd_output(&mut self, output: &str) {
        // $ cd /
        // $ ls
        // dir a
        // 14848514 b.txt
        // 8504156 c.dat
        // dir d
        // $ cd a
        // $ ls
        // dir e
        // 29116 f
        // 2557 g
        // 62596 h.lst
        // $ cd e
        // $ ls
        // 584 i
        // $ cd ..
        // $ cd ..
        // $ cd d
        // $ ls
        // 4060174 j
        // 8033020 d.log
        // 5626152 d.ext

        // The output is a list of commands and their output, every cmd starts with a $

        // Split the output into lines
        let mut current_dir = self.root.clone();
        for line in output.lines() {
            if line.starts_with("$") {

                // Split the line into command and arguments
                let mut parts = line.split_whitespace();
                // Skip initial $
                parts.next();
                let cmd = parts.next().unwrap();
                let args = parts.collect::<Vec<&str>>();
                match cmd {
                    "cd" => {
                        // Change directory
                        let dir_name = args[0];
                        if dir_name == "/" {
                            current_dir = self.root.clone();
                        } else if dir_name == ".." {
                            let parent = current_dir.borrow().parent.clone();
                            current_dir = parent.unwrap().clone();
                        } else {
                            // Add directory
                            let dir = Rc::new(RefCell::new(Directory::new(dir_name, Some(current_dir.clone()))));
                            current_dir.borrow_mut().add_directory(dir.clone());
                            current_dir = dir.clone()
                        }
                    },
                    "ls" => {
                    },
                    _ => panic!("Unknown command"),
                }
            } else {
                // It is a line of output from the command
                let mut parts = line.split_whitespace();
                let file_type = parts.next().unwrap();
                let file_name = parts.next().unwrap();
                match file_type {
                    "dir" => {
                    },
                    _ => {
                        // Add a file
                        let file_size = file_type.parse::<u64>().unwrap();
                        let file = File {
                            name: file_name.to_string(),
                            size: file_size,
                        };
                        current_dir.borrow_mut().add_file(file);
                    },
                }
            }
        }
    }
}



fn main() {
    let INPUT = include_str!("input.txt");
    let mut fs = FileSystem::new();
    fs.parse_cmd_output(INPUT);
    println!("Size of root: {}", fs.root.borrow().size());

    // Calculate the size of all directories below 100000 bytes
    let mut total_size = 0;
    for directory in fs.root.borrow().get_all_directories() {

        if directory.borrow().size() <= 100000 {
            total_size += directory.borrow().size();
        }
    }

    println!("Total size of directories below 100000 bytes: {}", total_size);

    // Total disk space
    let total_size = fs.root.borrow().size();
    let disk_size = 70000000;
    let update_size = 30000000;
    let required_size = disk_size - update_size;
    let to_delete = total_size - required_size;
    let mut smallest_directory : Option<Rc<RefCell<Directory>>> = None;
    for directory in fs.root.borrow().get_all_directories() {
        if directory.borrow().size() >= to_delete {
            if let Some(ref mut smallest) = smallest_directory {
                if directory.borrow().size() < smallest.borrow().size() {
                    *smallest = directory.clone();
                }
            } else {
                smallest_directory = Some(directory.clone());
            }
        }
    }

    if let Some(directory) = smallest_directory {
        println!("Smallest directory bigger than {} bytes: {}", to_delete, directory.borrow().name);
        println!("Size: {}", directory.borrow().size());
    }
}