<template>
  <div class="grade">
    <el-container>
      <el-header>
        <h1>选择年级</h1>
      </el-header>
      <el-main>
        <!-- 年级选择 -->
        <div>
          <el-radio label="1">一年级</el-radio>
        </div>
        <div>
          <el-radio label="2">二年级</el-radio>
        </div>
        <!-- 下一步 选择学期 -->
        <div style="margin: 100px"></div>
        <router-link to="/volume">
          <el-button type="primary" round>下一步</el-button>
        </router-link>
      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "Grade",
};
</script>
