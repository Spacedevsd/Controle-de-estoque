<script>
  import {
    Button,
    Container,
    Jumbotron,
    Row,
    Card,
    CardBody,
    CardFooter,
    Col,
    Input,
    InputGroup,
    Badge
  } from "sveltestrap";

  import { onMount } from "svelte";

  let products = [];

  let title = "";
  const server = "http://localhost:3001/api/v1";

  onMount(async () => {
    const response = await (await fetch(`${server}/products`)).json();
    products = response.products;
  });

  async function addProduct(ev) {
    ev.preventDefault();
    const response = await (await fetch(`${server}/products`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title })
    })).json();
    products = [...products, response.product];
    title = "";
  }

  async function stock(p) {
    const response = await (await fetch(`${server}/products`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ id: p.id, status: p.status })
    })).json();
    products[products.indexOf(p)] = response.product;
  }
</script>

<style>
  .cardDisabled {
    opacity: 0.6;
  }
</style>

<Container class="mt-5">
  <h4 class="text-center text-muted">Controle de Estoque</h4>
</Container>

<Jumbotron>
  <Container>
    <Row>
      <Col sm="12" class="mb-3">
        <h5 class="text-muted">
          Em estoque
          <Badge color="primary">
            {products.filter(p => (p.status ? p : 0)).length}
          </Badge>
        </h5>
      </Col>
      {#each products as product}
        <Col sm="12" lg="4" class="mb-3">
          <card
            class="card h-100 {product.status == false ? 'cardDisabled' : ''}">
            <CardBody>{product.title}</CardBody>
            <CardFooter class="text-right">
              <Button
                color="success"
                disabled={product.status}
                on:click={() => stock(product)}>
                <i class="fas fa-sync" />
              </Button>
              <Button
                color="info"
                disabled={!product.status}
                on:click={() => stock(product)}>
                <i class="fas fa-folder-open" />
              </Button>
            </CardFooter>
          </card>
        </Col>
      {/each}
    </Row>
  </Container>
</Jumbotron>

<Container>
  <form>
    <InputGroup>
      <Col>
        <Input placeholder="Insert a title" bind:value={title} autofocus />
      </Col>
    </InputGroup>
    <InputGroup class="text-right mt-3">
      <Col>
        <Button disabled={!title} color="success" on:click={addProduct}>
          Adicionar
        </Button>
      </Col>
    </InputGroup>
  </form>
</Container>
