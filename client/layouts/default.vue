<script setup>
import AppHeaderVue from '../components/AppHeader.vue'
import AppFooterVue from '../components/AppFooter.vue'
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
    display: flex;
    flex-direction: column;
    flex-grow: 1;
    flex-basis: auto;
}
</style>