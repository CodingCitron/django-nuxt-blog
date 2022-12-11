import instance from '..'

function signIn(data) {
    return instance.post('auth/sign-in', data)
}

function signUp(data) {
    return instance.post('auth/sign-up', data)
}

function signOut() {
    return instance.post('auth/sign-out')
}

export {
    signIn,
    signUp,
    signOut
}