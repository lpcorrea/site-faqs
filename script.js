const input = document.getElementById("searchInput");
const resultadosDiv = document.getElementById("resultados");
const listaMaisPesquisadas = document.getElementById("listaMaisPesquisadas");
const maisPesquisadasDiv = document.getElementById("maisPesquisadas");

// Array que vai armazenar as perguntas mais pesquisadas
let perguntasMaisPesquisadas = JSON.parse(localStorage.getItem("maisPesquisadas")) || [];

// Função para exibir as perguntas mais pesquisadas
function exibirMaisPesquisadas() {
  listaMaisPesquisadas.innerHTML = "";
  // Ordenar por número de marcas
  perguntasMaisPesquisadas.sort((a, b) => b.marcas - a.marcas);
  perguntasMaisPesquisadas.forEach((faq) => {
    const div = document.createElement("div");
    var linkTicket = "https://narwalsistemas.movidesk.com/Ticket/Edit/" + faq.id; // Link para o ticket
    div.className = "resultado";
    div.innerHTML = `
      <h2>Ticket: <a id="linkResultado" href=${linkTicket} target="_blank">${faq.id}</a></h2>
      <p><strong>Pergunta:</strong> ${faq.pergunta}</p>
      <p><strong>Causa raiz:</strong> ${faq.causa}</p>
      <p><strong>Solução:</strong> ${faq.solucao}</p>
    `;
    listaMaisPesquisadas.appendChild(div);
  });
}

// Função para normalizar o texto (remove acentos e converte para minúsculas)
function normalizarTexto(texto) {
  return texto
    .normalize("NFD")
    .replace(/\p{Diacritic}/gu, "")
    .toLowerCase()
    .trim();
}

// Função que verifica se todas as palavras do termo de pesquisa estão presentes na pergunta
function buscarFragmentos(termo, pergunta) {
  const palavrasTermo = termo.split(" ").map(normalizarTexto); // Divide o termo em palavras e normaliza
  const perguntaNormalizada = normalizarTexto(pergunta); // Normaliza a pergunta
  return palavrasTermo.every((palavra) => perguntaNormalizada.includes(palavra)); // Verifica todas as palavras
}

input.addEventListener("keypress", function (e) {
  if (e.key === "Enter") {
    const termo = normalizarTexto(this.value); // Normaliza o termo digitado
    resultadosDiv.innerHTML = ""; // Limpa resultados anteriores
    maisPesquisadasDiv.style.display = "none"; // Esconde as perguntas mais pesquisadas ao realizar uma pesquisa

    console.log("Termo de pesquisa:", termo); // Log do termo de pesquisa
    if (termo.length === 0) { 
      console.log("Campo de pesquisa vazio, exibindo perguntas mais pesquisadas.");
      exibirMaisPesquisadas(); 
      return;
    } // Se o termo estiver vazio, exibe as perguntas mais pesquisadas

    // Divida o termo em palavras
    const palavrasTermo = termo.split(" ").map(normalizarTexto);

    fetch("faq.json")
      .then((res) => res.json())
      .then((faqs) => {
        const encontrados = faqs.filter(faq =>
          buscarFragmentos(termo, faq.pergunta)
        );

        // Exibir resultados encontrados ou mensagem de erro
        if (encontrados.length === 0) {
          resultadosDiv.innerHTML = "<p>Nenhuma resposta encontrada.</p>";
        } else {
          encontrados.forEach(faq => {
            const div = document.createElement("div");
            var linkTicket = "https://narwalsistemas.movidesk.com/Ticket/Edit/" + faq.id;
            div.className = "resultado";
            div.innerHTML = `
              <h2>Ticket: <a id="linkResultado" href=${linkTicket} target="_blank">${faq.id}</a></h2>
              <p><strong>Pergunta:</strong> ${faq.pergunta}</p>
              <p><strong>Causa raiz:</strong> ${faq.causa}</p>
              <p><strong>Solução:</strong> ${faq.solucao}</p>
            `;
            //  <button class="marcar-btn"></button>
            
            resultadosDiv.appendChild(div);

            // Adicionar evento de clique no botão de marcar
            //const botao = div.querySelector(".marcar-btn");
            //botao.addEventListener("click", () => marcarComoResolvida(faq, botao));
          });
        }

        // Atualizar a lista das mais pesquisadas com a pergunta, causa e solução
        encontrados.forEach(faq => {
          // Verifica se a pergunta já foi registrada nas perguntas mais pesquisadas
          if (!perguntasMaisPesquisadas.some((item) => item.id === faq.id)) {
            perguntasMaisPesquisadas.push({
              id: faq.id,
              pergunta: faq.pergunta,
              causa: faq.causa,
              solucao: faq.solucao,
              marcas: 0, // Inicialmente sem marcas
            });

            // Limitar o número de perguntas mais pesquisadas a 5
            if (perguntasMaisPesquisadas.length > 5) {
              perguntasMaisPesquisadas.shift(); // Remove a mais antiga se houver mais de 5
            }

            localStorage.setItem("maisPesquisadas", JSON.stringify(perguntasMaisPesquisadas));
            exibirMaisPesquisadas(); // Atualiza a exibição das perguntas mais pesquisadas
          }
        });
      })
      .catch((err) => {
        console.error("Erro ao carregar FAQ:", err);
        resultadosDiv.innerHTML = "<p>Erro ao buscar as informações.</p>";
      });
  }
});

// Função para marcar uma solução como resolvida
function marcarComoResolvida(faq, botao) {
    // Verifica se já está na lista de mais pesquisadas
    let perguntaExistente = perguntasMaisPesquisadas.find((item) => item.id === faq.id);
  
    if (!perguntaExistente) {
      // Se ainda não estiver, adiciona com 1 marcação
      perguntaExistente = {
        id: faq.id,
        pergunta: faq.pergunta,
        causa: faq.causa,
        solucao: faq.solucao,
        marcas: 1
      };
      perguntasMaisPesquisadas.push(perguntaExistente);
    } else {
      // Se já existe, apenas incrementa a marcação
      perguntaExistente.marcas += 1;
    }
  
    // Reordenar e salvar
    perguntasMaisPesquisadas.sort((a, b) => b.marcas - a.marcas);
    localStorage.setItem("maisPesquisadas", JSON.stringify(perguntasMaisPesquisadas));
    exibirMaisPesquisadas();
  
    // Altera a cor do botão
    botao.style.backgroundColor = "#50fa7b";
    botao.disabled = true;
  }

// Evento de input para detectar quando o campo de pesquisa for apagado
input.addEventListener("input", function () {
  const termo = this.value.trim();

  if (termo === "") {
    // Se o campo de pesquisa estiver vazio, exibe as perguntas mais pesquisadas
    resultadosDiv.innerHTML = "";
    maisPesquisadasDiv.style.display = "block"; // Mostra as perguntas mais pesquisadas
    exibirMaisPesquisadas(); // Atualiza e ordena por marcações
  }
});

// Exibir perguntas mais pesquisadas ao carregar a página
exibirMaisPesquisadas();
