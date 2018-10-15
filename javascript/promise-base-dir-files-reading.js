const fs = require('fs');

const readDirAsync = (dirname) => {
    return new Promise((resolve, reject) => {  
        fs.readdir(dirname, 
            (err, files) => {
            if (err) {
                reject (err)
            } else {
                setTimeout(() => resolve(files), 1000) 
            }
        })
    })
}

const readFilesAsync = (dirname, files) => {
    return new Promise(async (resolve, reject) => {
        const filesdata = await Promise.all(
            // Passing a array of Promise, and return the 
            // the array of those Promise value. 
            files.map((file) => {
            return new Promise((resolve, reject) => {
                    fs.readFile(dirname + '/' + file, 'utf8', 
                        (err, data) => {
                            if (err) {
                                reject(err)
                            } else {
                                resolve(data)
                            }
                    })
                })
        }))
        resolve(filesdata)
    })
}


const getDirFiles = async () => {
    console.log("Waiting the readDirAsync Promise return...")
    const dirname = "vanilla-javascript" 
    const files =  await readDirAsync(dirname)
    const filesdata = await readFilesAsync(dirname, files)
    filesdata.forEach(filedata => console.log(filedata)) 
}

console.log("As Async read directory files, this line will be logged first.")

getDirFiles()
