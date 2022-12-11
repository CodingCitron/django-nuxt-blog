<script setup>
import { ref } from 'vue'
import { useContext } from '@nuxtjs/composition-api'

const { $axios } = useContext()

const username = ref(''),
password = ref(''),
confirmPassword = ref(''),
message = ref('')

function empty() {
    return (
        username.value.trim() === '' ||
        password.value.trim() === '' ||
        confirmPassword.value.trim() === ''
    )
}

async function signUpHandler() {
    if(empty()) return
    if(password.value !== confirmPassword.value) return

    const data = {
        username: username.value,
        password: password.value,
    }

    try {
        const res = await $axios.post('auth/sign-up', data)
        console.log(res)

    } catch (error) {
        console.log(error.message)
    }

}

</script>
<template>
    <div class="sign-up-container">
        <form class="form" @submit.prevent="signUpHandler">
            <div class="title">
                <h2>회원가입</h2>
            </div>
            <div>
                <input
                    type="text" 
                    class="form-item"
                    v-model="username"
                    placeholder="아이디"
                />
            </div>
            <div>
                <input
                    type="password" 
                    class="form-item"
                    v-model="password"
                    placeholder="비밀번호"
                />
            </div>
            <div>
                <input
                    type="password" 
                    class="form-item"
                    v-model="confirmPassword"
                    placeholder="비밀번호 확인"
                />
            </div>
            <div class="col">
                <button 
                    class="round-button"
                >   
                    회원가입
                </button>
                <nuxt-link 
                    to="/"
                    class="round-button"
                >
                    취소
                </nuxt-link> 
            </div>
        </form>
    </div>
</template>
<style scoped>
.form {
    width: 280px;
}

.title {
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 16px;
    text-align: left;
}

.form-item {
    margin-bottom: 10px;
}

.round-button {
    padding: 8px;
    margin-bottom: 10px;
    color: white;
    text-align: center;
}
</style>