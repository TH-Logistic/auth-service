const user = process.env.MONGO_USER
const password = process.env.MONGO_PASSWORD
const database = process.env.MONGO_INITDB_DATABASE

// Create user if needed

// db.createUser({
//     user: user,
//     pwd: password,
//     roles: [
//         {
//             role: "readWrite",
//             db: database
//         }
//     ]
// })