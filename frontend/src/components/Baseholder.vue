<template>
  <div v-if="hasParams()">
    <b-card 
      style="width: 20rem" 
      class="text-center" 
      v-bind:header= "property.name"
      border-variant="dark"
      bg-variant="light">
    <b-card-text class="text-left">
    <p><b>Summary</b></p>
      {{property.description}}
    </b-card-text>
    <b-button v-bind:to="link">To club Page</b-button>
  </b-card>
    
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: 'Baseholder',
  props: ['items'],
  data: function() {
    return {
      property: this.items
    }
  },
  methods:
  {
      hasParams: function() 
      {
          if(this.property && this.property.name
            && this.property.description)
            {
                return true;
            }
            return false;
      }

  },
  computed:
  {
      link: function()
      {
          return "club/" + this.items.name;
      }

  }
}

</script scoped>
.card {
  border: 2px;
}
</style>