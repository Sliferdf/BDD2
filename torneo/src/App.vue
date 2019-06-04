<template>
  <v-app id="inspire" dark>
    <v-navigation-drawer
      v-model="drawer"
      clipped
      fixed
      app
    >
      <v-list dense>
        <v-list-tile @click="">
          <v-list-tile-action>
            <v-icon>perm_identity</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Jugadores</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile @click="">
          <v-list-tile-action>
            <v-icon>local_bar</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Torneo</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
          <v-list-tile @click="">
          <v-list-tile-action>
            <v-icon>reorder</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Draws</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar app fixed clipped-left>
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>Torneo Tapitas 2019</v-toolbar-title>
    </v-toolbar>
    <v-footer app fixed>
      <span>&copy; 2019--Unaula--</span>
    </v-footer>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld'

export default {
  name: 'App',
  components: {
    HelloWorld
  },
  data () {
    return {
      drawer: null
    }
  }
}
</script>
