<template>
  <header class="navbar">
    <img src="./assets/vue.svg" alt="Logo" class="logo">
    <nav class="nav-center">
      <RouterLink to="/" class="nav-link" v-slot="{ isActive }">
        <span :class="{ 'active': isActive }">首页</span>
      </RouterLink>
      <RouterLink to="/changedetectHome" class="nav-link" v-slot="{ isActive }">
        <span :class="{ 'active': isActive }">变化检测</span>
      </RouterLink>
      <RouterLink to="/objectdetectHome" class="nav-link" v-slot="{ isActive }">
        <span :class="{ 'active': isActive }">目标检测</span>
      </RouterLink>
      <RouterLink to="/roadextractHome" class="nav-link" v-slot="{ isActive }">
        <span :class="{ 'active': isActive }">道路提取</span>
      </RouterLink>
      <RouterLink to="/landclassHome" class="nav-link" v-slot="{ isActive }">
        <span :class="{ 'active': isActive }">地物分类</span>
      </RouterLink>
    </nav>
  </header>
  <main class="main-content">
    <RouterView />
  </main>
</template>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #79879f; /* 更深的背景色 */
  padding: 1rem 2rem; /* 增加内边距 */
  box-shadow: 0px 4px 8px rgba(112, 173, 197, 0.2); /* 加深阴影效果 */
}

.logo {
  height: 90%;
  padding: 0.5em;
  will-change: filter;
  transition: filter 300ms;
}

.logo:hover {
  filter: drop-shadow(0 0 2em #ffffffaa); /* 更改悬停时的阴影颜色 */
}

.nav-center {
  display: flex;
  justify-content: center;
  gap: 1.5rem; /* 增加间距 */
}

.nav-link {
  text-decoration: none;
  color: #ffffff; /* 更改文字颜色为白色 */
  font-size: 1.2rem; /* 增大字体大小 */
  font-weight: 500; /* 更改字体粗细 */
  transition: color 0.3s ease, transform 0.3s ease; /* 添加过渡效果 */
}

.nav-link:hover {
  color: #007bff; /* 更改悬停时的文字颜色 */
  transform: translateY(-3px); /* 添加悬停时的下移效果 */
}

.active { /* 高亮当前激活的路由 */
  color: #007bff;
  font-weight: bold;
  border-bottom: 2px solid #007bff; /* 添加底部边框 */
}
</style>