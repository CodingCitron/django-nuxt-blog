<script setup>
import AppHeaderVue from '../components/common/AppHeader.vue'
import AppFooterVue from '../components/common/AppFooter.vue'
</script>
<template>
    <div class="container">
      <AppHeaderVue />
      <Nuxt />
      <AppFooterVue />
    </div>
</template>
<style scoped>
.container {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100vh;
}
</style>