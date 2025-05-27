#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

struct DataRow {
  std::string country;
  std::string region;
  int rank_felicidade;
  double score_felicidade;
  double stand_error;
  double PIB;
  double family;
  double expect_vida;
  double freedom;
  double currupcao;
  double generosity;
  double dystopia;
  int country_code;
};

std::vector<std::string> split(const std::string &s, char delimiter) {
  std::vector<std::string> tokens;
  std::string token;
  std::istringstream tokenStream(s);
  while (std::getline(tokenStream, token, delimiter)) {
    tokens.push_back(token);
  }
  return tokens;
}

int main() {
  std::ifstream file("database/mundo_feliz.csv");
  std::string line;
  std::vector<DataRow> dataset;

  if (!file.is_open()) {
    std::cerr << "Erro ao abrir o arquivo!" << std::endl;
    return 1;
  }

  // Lê o cabeçalho
  std::getline(file, line);

  std::unordered_map<std::string, int> country_codes;
  int next_code = 0;

  while (std::getline(file, line)) {
    auto cols = split(line, ',');
    if (cols.size() != 12)
      continue;

    DataRow row;
    row.country = cols[0];
    row.region = cols[1];
    row.rank_felicidade = std::stoi(cols[2]);
    row.score_felicidade = std::stod(cols[3]);
    row.stand_error = std::stod(cols[4]);
    row.PIB = std::stod(cols[5]);
    row.family = std::stod(cols[6]);
    row.expect_vida = std::stod(cols[7]);
    row.freedom = std::stod(cols[8]);
    row.currupcao = std::stod(cols[9]);
    row.generosity = std::stod(cols[10]);
    row.dystopia = std::stod(cols[11]);

    // Converter país em categoria
    if (country_codes.find(row.country) == country_codes.end()) {
      country_codes[row.country] = next_code++;
    }
    row.country_code = country_codes[row.country];

    dataset.push_back(row);
  }

  // Exibe info geral
  std::cout << "Total de linhas: " << dataset.size() << std::endl;
  std::cout << "Total de colunas: 12 + 1 (country_code)" << std::endl;
  std::cout << "Primeiros 5 registros:\n";

  for (size_t i = 0; i < std::min(dataset.size(), size_t(5)); ++i) {
    const auto &row = dataset[i];
    std::cout << row.country << " (" << row.country_code << "), " << row.region
              << ", Rank: " << row.rank_felicidade
              << ", Score: " << row.score_felicidade << "\n";
  }

  return 0;
}
