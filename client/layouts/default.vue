<script setup>
import AppHeaderVue from '../components/common/AppHeader.vue'
import AppFooterVue from '../components/common/AppFooter.vue'
</script>
<template>
    <div class="wrap">
        <AppHeaderVue />
        <main>
            <Nuxt />
        </main>
        <AppFooterVue />
    </div>
</template>
<style scoped>
.wrap {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 100vh;
}

main {
    height: 100%;
    flex-grow: 2;
    flex-basis: auto;
}
</style>