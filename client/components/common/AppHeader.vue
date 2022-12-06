<script setup>

</script>
<template>
    <header>
        <h1>
            <nuxt-link to="/">LOGO</nuxt-link>
        </h1>
        <nav>
            <ul class="menu">
                <li>
                    <nuxt-link to="signin">로그인</nuxt-link>
                </li>
                <li>
                    <nuxt-link to="signup">회원가입</nuxt-link>
                </li>
            </ul>
        </nav>
    </header>
</template>
<style scoped>
header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    min-height: 40px;
    height: 40px;
    padding: 4px 6px;
}

.menu {
    display: flex;
    gap: 4px;
}
</style>