<script setup>
import { ref } from 'vue'
import axios from 'axios'

const username = ref('')
const password = ref('')

let config = {
    headers: {
        'Content-Type': 'application/json; charset=utf-8',
    },
}

async function submitHandler(){
    try {
        const res = await axios.post(
            'http://127.0.0.1:8000/api/auth/sign-in',
            {
                username: username.value,
                password: password.value
            },
            config
        )

        console.log(res)
    } catch (error) {
        console.log(error)
    }
}
</script>
<template>
    <form class="form" @submit.prevent="submitHandler">
        로그인
        <div>
            <input
                type="text" 
                class="form-item"
                v-model="username"
            />
        </div>
        <div>
            <input
                type="password" 
                class="form-item"
                v-model="password"
            />
        </div>
        <div>
            <button>제출</button>
        </div>
    </form>
</template>
<style scoped>
.form-item {
    border: 1px solid black;
}
</style>