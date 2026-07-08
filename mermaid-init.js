// Initialize mermaid and convert code blocks
document.addEventListener('DOMContentLoaded', function() {
    // Find all code blocks with language-mermaid class
    document.querySelectorAll('code.language-mermaid, code[class*="mermaid"]').forEach(function(code) {
        var pre = code.parentElement;
        if (pre && pre.tagName === 'PRE') {
            // Skip if already converted
            if (pre.className.includes('mermaid')) return;

            pre.className = 'mermaid';
            pre.textContent = code.textContent;

            // Remove the code element
            code.remove();
        }
    });

    // Initialize mermaid with configuration
    mermaid.initialize({
        startOnLoad: true,
        theme: document.documentElement.classList.contains('ayu') ? 'dark' :
               document.documentElement.classList.contains('coal') ? 'dark' :
               document.documentElement.classList.contains('navy') ? 'dark' :
               'default',
        securityLevel: 'loose',
        flowchart: {
            htmlLabels: true,
            curve: 'basis'
        },
        er: {
            useMaxWidth: false
        }
    });
});
