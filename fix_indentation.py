#!/usr/bin/env python3
"""
Script para corrigir problemas de indentação no arquivo main.py
Avila Transportes - Sistema de Cotação e Ordem de Coleta
"""

import re
import os
import shutil
import sys

def fix_indentation_in_file(filepath):
    """
    Corrige problemas de indentação em um arquivo Python.
    Foca especificamente em corrigir a função campos_cliente.
    """
    print(f"🔧 Corrigindo indentação em {filepath}...")
    
    # Fazer backup do arquivo original
    backup_file = f"{filepath}.bak"
    print(f"📑 Criando backup em {backup_file}")
    shutil.copy2(filepath, backup_file)
    
    # Ler o arquivo
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Flag para indicar se estamos dentro da função que precisa ser corrigida
    in_target_function = False
    function_start_line = -1
    fixed_lines = []
    
    for i, line in enumerate(lines):
        # Detectar início da função campos_cliente
        if re.match(r'^def\s+campos_cliente\s*\(', line):
            in_target_function = True
            function_start_line = i
            fixed_lines.append(line)  # Adiciona a linha de definição da função como está
            continue
        
        # Se estamos na função alvo, corrigir a indentação
        if in_target_function:
            # Verificar se saímos da função (encontramos outra função ou linha sem indentação)
            if re.match(r'^def\s+', line) or (line.strip() and line[0] not in ' \t'):
                in_target_function = False
                fixed_lines.append(line)  # Adiciona a linha como está
                continue
            
            # Corrigir indentação dentro da função
            if line.strip():  # Se a linha não estiver vazia
                # Remove toda a indentação existente
                stripped_line = line.lstrip()
                
                # Determinar o nível de indentação com base no conteúdo
                indent_level = 1  # Nível base para o corpo da função
                
                # Aumentar indentação para blocos com: with, if, for, while, etc.
                if "with col" in stripped_line:
                    indent_level = 2
                # Para linhas que estão dentro de blocos como with
                elif any(keyword in stripped_line for keyword in ['st.text_input', 'st.selectbox', 'value=', 'key=']):
                    indent_level = 3
                
                # Aplicar indentação correta (4 espaços por nível)
                fixed_line = ' ' * (4 * indent_level) + stripped_line
                fixed_lines.append(fixed_line)
            else:
                # Manter linhas vazias como estão
                fixed_lines.append(line)
        else:
            # Manter linhas fora da função alvo como estão
            fixed_lines.append(line)
    
    # Escrever o arquivo corrigido
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(fixed_lines)
    
    print(f"✅ Arquivo corrigido com sucesso!")
    print(f"🔍 Verificando se a correção funcionou...")
    
    # Verificar se o arquivo pode ser importado sem erros
    original_dir = os.getcwd()
    file_dir = os.path.dirname(os.path.abspath(filepath))
    
    try:
        os.chdir(file_dir)
        module_name = os.path.basename(filepath).replace('.py', '')
        
        # Limpar o cache de importação para garantir que o módulo seja recarregado
        if module_name in sys.modules:
            del sys.modules[module_name]
        
        # Tentar importar o módulo
        __import__(module_name)
        print(f"🎉 O arquivo {filepath} foi corrigido com sucesso e não contém erros de sintaxe!")
        success = True
    except Exception as e:
        print(f"❌ Ainda há erros no arquivo: {e}")
        print("Restaurando backup...")
        shutil.copy2(backup_file, filepath)
        success = False
    finally:
        os.chdir(original_dir)
    
    return success

def main():
    filepath = "main.py"
    if not os.path.exists(filepath):
        print(f"❌ Arquivo {filepath} não encontrado!")
        return False
    
    return fix_indentation_in_file(filepath)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
