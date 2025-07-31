#!/usr/bin/env python3
"""
Script de teste para verificar se o sistema está pronto para deploy
Avila Transportes - Sistema de Cotação e Ordem de Coleta
"""

import sys
import importlib.util
import os
import traceback
import re

def check_dependency(name):
    """Verifica se uma dependência está instalada"""
    try:
        spec = importlib.util.find_spec(name)
        if spec is None:
            return False
        return True
    except ImportError:
        return False

def check_file_exists(filepath):
    """Verifica se um arquivo existe"""
    return os.path.exists(filepath)

def inspect_indentation_error(file_path, line_number):
    """Analisa erros de indentação fornecendo contexto"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Determina o intervalo de linhas para exibir (5 linhas antes e depois do erro)
        start_line = max(0, line_number - 5)
        end_line = min(len(lines), line_number + 5)
        
        result = [f"\n🔍 Contexto do erro (linha {line_number}):\n"]
        
        # Adiciona linhas de contexto
        for i in range(start_line, end_line):
            prefix = "→ " if i == line_number - 1 else "  "
            line_content = lines[i].rstrip('\n')
            result.append(f"{prefix}{i+1}: {repr(line_content)}")
        
        # Tenta identificar o tipo de problema de indentação
        if line_number > 0 and line_number <= len(lines):
            problem_line = lines[line_number - 1]
            indent_spaces = len(problem_line) - len(problem_line.lstrip())
            
            # Verifica a indentação das linhas anteriores
            if line_number > 1:
                prev_line = lines[line_number - 2]
                prev_indent = len(prev_line) - len(prev_line.lstrip())
                
                if indent_spaces < prev_indent:
                    result.append(f"\n⚠️ Possível problema: A linha {line_number} tem {indent_spaces} espaços de indentação, enquanto a linha anterior tem {prev_indent}.")
                    result.append("   Verifique se a desindentação está correta ou se há uma mistura de tabs e espaços.")
        
        return "\n".join(result)
    except Exception as e:
        return f"Não foi possível analisar o arquivo: {e}"

def main():
    print("🚚 AVILA TRANSPORTES - TESTE PRÉ-DEPLOY")
    print("=" * 50)
    
    # Verificar dependências
    dependencies = ['streamlit', 'pandas', 'fpdf', 'requests', 'sqlite3']
    print("\n📦 Verificando dependências:")
    
    all_deps_ok = True
    for dep in dependencies:
        if check_dependency(dep):
            print(f"✅ {dep}")
        else:
            print(f"❌ {dep} - NÃO INSTALADO")
            all_deps_ok = False
    
    # Verificar arquivos necessários
    required_files = [
        'main.py',
        'requirements.txt',
        'Procfile',
        'runtime.txt',
        'CNAME',
        'index.html',
        'README.md',
        '.gitignore'
    ]
    
    print("\n📁 Verificando arquivos:")
    all_files_ok = True
    for file in required_files:
        if check_file_exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} - NÃO ENCONTRADO")
            all_files_ok = False
    
    # Verificar código principal
    print("\n🐍 Verificando código principal:")
    try:
        import main
        print("✅ main.py - Sem erros de sintaxe")
        code_ok = True
    except IndentationError as e:
        # Captura específica para erros de indentação
        filename = e.filename
        lineno = e.lineno
        print(f"❌ main.py - Erro de indentação na linha {lineno}: {e}")
        print(inspect_indentation_error(filename, lineno))
        code_ok = False
    except Exception as e:
        # Detecta se é um erro de indentação a partir da mensagem
        error_str = str(e)
        if "unindent does not match" in error_str or "unexpected indent" in error_str:
            match = re.search(r'\((.+?), line (\d+)\)', error_str)
            if match:
                filename, lineno = match.groups()
                lineno = int(lineno)
                print(f"❌ main.py - Erro de indentação na linha {lineno}: {error_str}")
                print(inspect_indentation_error(filename, lineno))
            else:
                print(f"❌ main.py - Erro de indentação: {error_str}")
                print(traceback.format_exc())
        else:
            print(f"❌ main.py - Erro: {e}")
            print(traceback.format_exc())
        code_ok = False
    
    # Resultado final
    print("\n" + "=" * 50)
    if all_deps_ok and all_files_ok and code_ok:
        print("🎉 SISTEMA PRONTO PARA DEPLOY!")
        print("\n📋 Próximos passos:")
        print("1. Instale o Git (se não tiver)")
        print("2. Siga o GUIA_DEPLOY_COMPLETO.md")
        print("3. Faça o deploy no Streamlit Cloud")
        print("\n🌐 URLs finais:")
        print("- Landing: https://avilatransportes.com.br")
        print("- Sistema: https://avilatransportes-sistema.streamlit.app")
        return True
    else:
        print("❌ SISTEMA NÃO ESTÁ PRONTO")
        print("\n🔧 Corrija os problemas acima antes do deploy")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
